"""Validate the actual deployment artifact using Python standard library only."""
from html.parser import HTMLParser
from pathlib import Path
import json, re, xml.etree.ElementTree as ET
root=Path('dist')
html=(root/'index.html').read_text()
class Audit(HTMLParser):
 def __init__(self):
  super().__init__(); self.ids=[];self.hrefs=[];self.images=[];self.headings=[];self.canonicals=[];self.metas={};self.script_type=None;self.schemas=[];self.data='';self.article=None;self.people=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  assert not any(k.startswith('on') for k in a), f'Inline event handler on {tag}'
  if 'id' in a:self.ids.append(a['id'])
  if tag=='a':self.hrefs.append(a.get('href',''))
  if tag=='img':self.images.append(a)
  if tag in ['h1','h2','h3']:self.headings.append(int(tag[1]))
  if tag=='link' and a.get('rel')=='canonical':self.canonicals.append(a['href'])
  if tag=='meta':self.metas[a.get('name',a.get('property'))]=a.get('content','')
  if tag=='script':self.script_type=a.get('type');self.data='';assert self.script_type=='application/ld+json','No runtime JS needed'
 def handle_data(self,data):
  if self.script_type:self.data+=data
 def handle_endtag(self,tag):
  if tag=='script':self.schemas.append(json.loads(self.data));self.script_type=None
p=Audit();p.feed(html)
assert not re.search('jayna',html,re.I)
assert p.headings.count(1)==1 and all(b<=a+1 for a,b in zip(p.headings,p.headings[1:]))
assert len(p.ids)==len(set(p.ids))
assert p.canonicals==['https://wmiegroup.com/']
for href in p.hrefs:
 assert href
 if href.startswith('#'):assert href[1:] in p.ids,href
 elif not re.match(r'(https://|mailto:)',href):assert (root/href.lstrip('/')).exists(),href
for im in p.images:
 assert im.get('alt') and im.get('width') and im.get('height')
 assert (root/im['src']).exists()
for name in ['description','og:title','og:description','og:url','og:image','twitter:title','twitter:description','twitter:card']:
 assert p.metas.get(name),name
schema=p.schemas[0]
roles=schema['@graph'][0]['member']
assert [r['member']['name'] for r in roles]==['Todd Segress','Janie','David']
assert all(r['roleName']=='Co-Owner' for r in roles)
assert html.count('<p>Co-Owner</p>')==3
assert 'display:none' not in html and 'overflow:hidden' not in html.split('body{')[1].split('}')[0]
assert 'Sitemap: https://wmiegroup.com/sitemap.xml' in (root/'robots.txt').read_text()
urls=ET.parse(root/'sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
assert [u.text for u in urls]==['https://wmiegroup.com/']
assert not any('jayna' in str(f).lower() for f in root.rglob('*'))
assert 'noindex' in (root/'404.html').read_text()
assert (root/'assets/social-preview.jpg').read_bytes()[:2]==b'\xff\xd8'
print(f'PASS: ownership, schema JSON, sitemap XML, metadata, {len(p.hrefs)} links, {len(p.images)} images, heading hierarchy, no hidden sections, deployment allowlist.')
