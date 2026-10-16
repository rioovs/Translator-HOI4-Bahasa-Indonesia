const fs = require('fs');
const p1 = JSON.parse(fs.readFileSync('scripts/focus_part1_extracted.json', 'utf8'));

const content = fs.readFileSync('scripts/make_focus_part1.js', 'utf8');
const start = content.indexOf('const trans = {');
const end = content.indexOf('// Check coverage against p1');
let trans;
eval(content.substring(start, end).replace('const trans =', 'trans ='));

const missing = p1.filter(it => !trans[it.key]);
console.log('Missing count:', missing.length);
missing.forEach((it, idx) => {
  console.log(`[${idx + 1}] ${it.key}: ${JSON.stringify(it.val)}`);
});
