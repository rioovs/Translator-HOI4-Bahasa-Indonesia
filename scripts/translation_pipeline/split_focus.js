const fs = require('fs');
const src = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/focus_l_english.yml';
const lines = fs.readFileSync(src, 'utf8').split(/\r?\n/);

const items = [];

for (let i = 1; i < lines.length; i++) {
  const line = lines[i];
  if (!line.trim() || line.trim().startsWith('#')) continue;
  const colon = line.indexOf(':');
  if (colon === -1) continue;
  
  const key = line.substring(0, colon).trim();
  const after = line.substring(colon + 1);
  const q1 = after.indexOf('"');
  const q2 = after.lastIndexOf('"');
  if (q1 === -1 || q2 <= q1) continue;
  
  const val = after.substring(q1 + 1, q2);
  const isPureVar = /^\$[A-Za-z0-9_]+\$$/.test(val.trim());
  
  items.push({
    lineNum: i + 1,
    key,
    val,
    isPureVar
  });
}

console.log('Total items extracted:', items.length);
console.log('Pure var items:', items.filter(x => x.isPureVar).length);
console.log('Items needing translation:', items.filter(x => !x.isPureVar).length);

// Let's divide into 6 logical parts of ~400 translation items each
const transItems = items.filter(x => !x.isPureVar);
const partSize = Math.ceil(transItems.length / 6);

const parts = [[], [], [], [], [], []];
transItems.forEach((it, idx) => {
  const p = Math.min(5, Math.floor(idx / partSize));
  parts[p].push(it);
});

parts.forEach((p, idx) => {
  console.log(`Part ${idx + 1}: ${p.length} items (lines ${p[0].lineNum} to ${p[p.length - 1].lineNum})`);
  fs.writeFileSync(`scripts/focus_part${idx + 1}_extracted.json`, JSON.stringify(p, null, 2), 'utf8');
});

// Also save pure vars map for preservation
const pureVars = {};
items.filter(x => x.isPureVar).forEach(it => {
  pureVars[it.key] = it.val;
});
fs.writeFileSync('scripts/focus_pure_vars.json', JSON.stringify(pureVars, null, 2), 'utf8');
console.log('Saved focus_pure_vars.json with', Object.keys(pureVars).length, 'entries.');
