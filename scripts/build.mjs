import {mkdir, rm, copyFile} from 'node:fs/promises';
const assets=['todd.webp','janie.webp','david.webp','logo-96.webp','social-preview.jpg'];
await rm('dist',{recursive:true,force:true});
await mkdir('dist/assets',{recursive:true});
for(const file of ['index.html','robots.txt','sitemap.xml','404.html']) await copyFile(file,`dist/${file}`);
for(const file of assets) await copyFile(`assets/${file}`,`dist/assets/${file}`);
console.log('Built static site: 9 public files; original/historical assets excluded.');
