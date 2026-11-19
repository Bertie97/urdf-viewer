from pathlib import Path
root=Path(__file__).resolve().parent.parent
html=(root/'index.html').read_text().replace('<meta charset="utf-8">','<meta charset="utf-8"><base href="/">',1)
check='''
const result=document.createElement('pre');result.id='test-result';result.style.cssText='position:fixed;bottom:0;left:0;background:#14212c;color:white;padding:12px;z-index:100';document.body.append(result);
try {
 while(loadedComponents.size<59)await new Promise(resolve=>setTimeout(resolve,100));
 const paths=['e05_pro.urdf',...['base_link','Link1','Link2','Link3','Link4','Link5','Link6','end_Link'].map(n=>'meshes/'+n+'.STL')];
 const files=await Promise.all(paths.map(async path=>{const response=await fetch('models/e05_pro/'+path);if(!response.ok)throw Error(path);const file=new File([await response.blob()],path.split('/').at(-1));Object.defineProperty(file,'webkitRelativePath',{value:'e05_pro/'+path});return file}));
 await importModel(files);
 if(COMP.Link1.length!==25||COMP.Link3.length!==28)throw Error('component counts incorrect');
 if(document.querySelectorAll('.joint-label').length!==7)throw Error('joint labels missing');
 result.textContent='PASS: E05 directory import; Link1 25, Link3 28; '+s.textContent;
 document.body.dataset.testResult='PASS';
}catch(error){result.textContent='FAIL: '+error.stack;document.body.dataset.testResult='FAIL'}
'''
html=html.replace('</script>', '</script>',1)
idx=html.rindex('</script>');html=html[:idx]+check+html[idx:]
(root/'tests/import-check.html').write_text(html)
