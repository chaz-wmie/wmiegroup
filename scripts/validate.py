"""Validate all deployable pages using the Python standard library."""
from html.parser import HTMLParser
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
from urllib.parse import urlsplit
root=Path('dist');origin='https://wmiegroup.com'
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.links=[];self.images=[];self.headings=[];self.canonical=[];self.meta={};self.scripts=[];self.type=None;self.data='';self.title='';self.in_title=False;self.forms=[];self.labels=[];self.inputs=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  assert not any(k.startswith('on') for k in a),f'Inline event on {t}'
  if a.get('id'):self.ids.append(a['id'])
  if t=='a':self.links.append(a.get('href',''))
  if t=='img':self.images.append(a)
  if t in ['h1','h2','h3']:self.headings.append(int(t[1]))
  if t=='link':
   if a.get('rel')=='canonical':self.canonical.append(a['href'])
   if a.get('rel') in ['stylesheet','icon']:self.links.append(a['href'])
  if t=='meta':self.meta[a.get('name',a.get('property'))]=a.get('content')
  if t=='script':
   self.type=a.get('type');self.data=''
   if a.get('src'):self.links.append(a['src'])
  if t=='title':self.in_title=True
  if t=='form':self.forms.append(a)
  if t=='label':self.labels.append(a.get('for'))
  if t in ['input','select','textarea']:self.inputs.append(a)
 def handle_data(self,d):
  if self.type=='application/ld+json':self.data+=d
  if self.in_title:self.title+=d
 def handle_endtag(self,t):
  if t=='script':
   if self.type=='application/ld+json':self.scripts.append(json.loads(self.data))
   self.type=None
  if t=='title':self.in_title=False
parsed={};titles=[];descs=[]
for f in root.rglob('index.html'):
 p=Page();h=f.read_text();p.feed(h);path='/'+str(f.parent.relative_to(root)).strip('.')+'/' if f.parent!=root else '/'
 path=path.replace('//','/');parsed[path]=p
 assert not re.search('jayna',h,re.I),f
 assert p.headings.count(1)==1 and all(b<=a+1 for a,b in zip(p.headings,p.headings[1:])),(f,p.headings)
 assert len(p.ids)==len(set(p.ids)),f
 assert p.canonical==[origin+path],(f,p.canonical,path)
 assert p.scripts and p.scripts[0]['@context']=='https://schema.org'
 roles=p.scripts[0]['@graph'][0]['member']
 assert [r['member']['name'] for r in roles]==['Todd Segress','Janie Meadows','David Stephens']
 assert all(r['roleName']=='Co-Owner' for r in roles)
 for key in ['description','og:title','og:description','og:url','og:image','twitter:title','twitter:description','twitter:card']:
  assert p.meta.get(key),(f,key)
 titles.append(p.title);descs.append(p.meta['description'])
 for im in p.images:
  assert im.get('alt') and im.get('width') and im.get('height')
  assert (root/im['src'].lstrip('/')).exists()
assert len(titles)==len(set(titles)) and len(descs)==len(set(descs))
links=0
for path,p in parsed.items():
 for link in p.links:
  links+=1;assert link
  u=urlsplit(link)
  if u.scheme in ['https','mailto']:continue
  target=u.path or path
  if target in parsed:
   if u.fragment:assert u.fragment in parsed[target].ids,(path,link)
  else:assert (root/target.lstrip('/')).is_file(),(path,link)
contact=parsed['/contact/'];form=contact.forms[0]
assert form['method']=='POST' and form['data-netlify']=='true' and form['netlify-honeypot']=='bot-field' and form['action']=='/thank-you/'
assert 'hidden' in form,'Form must stay unavailable until registration verified'
for field in contact.inputs:
 if field.get('id'):assert field['id'] in contact.labels
assert any(i.get('name')=='form-name' and i.get('value')=='business-opportunity' for i in contact.inputs)
assert any(i.get('name')=='bot-field' for i in contact.inputs)
assert parsed['/thank-you/'].meta['robots']=='noindex'
assert 'noindex' in (root/'404.html').read_text()
urls=[x.text for x in ET.parse(root/'sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert sorted(urls)==sorted(origin+p for p,v in parsed.items() if v.meta.get('robots')!='noindex')
assert 'Sitemap: '+origin+'/sitemap.xml' in (root/'robots.txt').read_text()
assert not any('jayna' in str(f).lower() for f in root.rglob('*'))
assert (root/'assets/social-preview.jpg').read_bytes()[:2]==b'\xff\xd8'
assert 'data-netlify' in (root/'assets/contact.js').read_text()
print(f'PASS: {len(parsed)} pages, {len(urls)} indexable URLs, {links} links/assets, unique metadata, ownership, headings, schema, XML sitemap, accessible form fields, honeypot and safe fallback.')
