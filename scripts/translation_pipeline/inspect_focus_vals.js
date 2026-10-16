const fs = require('fs');
const src = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/focus_l_english.yml';
const lines = fs.readFileSync(src, 'utf8').split(/\r?\n/);

let pureVars = 0;
let emptyVal = 0;
let textVal = 0;

for (let i = 1; i < lines.length; i++) {
  const line = lines[i];
  if (!line.trim() || line.trim().startsWith('#')) continue;
  const colon = line.indexOf(':');
  if (colon === -1) continue;
  const after = line.substring(colon + 1);
  const q1 = after.indexOf('"');
  const q2 = after.lastIndexOf('"');
  if (q1 === -1 || q2 <= q1) {
    emptyVal++;
    continue;
  }
  const val = after.substring(q1 + 1, q2);
  if (/^\$[A-Za-z0-9_]+\$$/.test(val.trim())) {
    pureVars++;
  } else {
    textVal++;
  }
}

console.log('Text values to translate:', textVal);
console.log('Pure variables:', pureVars);
console.log('Empty values:', emptyVal);
