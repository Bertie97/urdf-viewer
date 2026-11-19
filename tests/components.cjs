const fs=require('node:fs'),assert=require('node:assert/strict'),vm=require('node:vm');
const source=fs.readFileSync('index.html','utf8');const start=source.indexOf('function connectedTriangles('),end=source.indexOf('async function splitImportedMeshes',start);
vm.runInThisContext(source.slice(start,end));
assert.equal(connectedTriangles(new Float32Array([0,0,0,1,0,0,0,1,0, 1,0,0,1,1,0,0,1,0, 4,0,0,5,0,0,4,1,0])).length,2);
assert.equal(connectedTriangles(new Float32Array()).length,0);
for(const name of ['Link1','Link3']){
 const b=fs.readFileSync(`models/e05_pro/meshes/${name}.STL`),count=b.readUInt32LE(80),p=new Float32Array(count*9);
 for(let t=0;t<count;t++)for(let k=0;k<9;k++)p[t*9+k]=b.readFloatLE(84+t*50+12+k*4);
 const groups=connectedTriangles(p);assert.equal(groups.reduce((sum,g)=>sum+g.length,0),count);console.log(name,groups.length,'components',count,'triangles');
 assert.equal(groups.length,name==='Link1'?25:28);
}
console.log('Connectivity and triangle preservation: PASS');
