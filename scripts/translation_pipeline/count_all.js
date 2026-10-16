const fs = require('fs');
const p = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por';
const files = fs.readdirSync(p);
let totalLines = 0;
let totalKeys = 0;
for (const f of files) {
  const content = fs.readFileSync(p + '/' + f, 'utf8');
  const lines = content.split('\n');
  totalLines += lines.length;
  const keyRe = new RegExp('^\\s*[A-Za-z0-9_]+:\\d*\\s*"');
  const keys = lines.filter(function(l) { return keyRe.test(l); });
  totalKeys += keys.length;
}
console.log('Total files: ' + files.length);
console.log('Total lines: ' + totalLines);
console.log('Total keys: ' + totalKeys);
