const fs = require('fs');
const src = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/focus_l_english.yml';
const lines = fs.readFileSync(src, 'utf8').split(/\r?\n/);

const prefixes = {};
let count = 0;
const entries = [];

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  if (i === 0 || !line.trim() || line.trim().startsWith('#')) continue;
  
  const colon = line.indexOf(':');
  if (colon === -1) continue;
  
  const key = line.substring(0, colon).trim();
  const rest = line.substring(colon + 1);
  const q1 = rest.indexOf('"');
  const q2 = rest.lastIndexOf('"');
  if (q1 === -1 || q2 <= q1) continue;
  
  const val = rest.substring(q1 + 1, q2);
  
  // Tag / prefix
  let prefix = key.split('_')[0];
  prefixes[prefix] = (prefixes[prefix] || 0) + 1;
  count++;
  entries.push({ lineNum: i + 1, key, val });
}

console.log('Total valid key-value pairs:', count);
const sortedPrefixes = Object.entries(prefixes).sort((a, b) => b[1] - a[1]);
console.log('Top prefixes:', sortedPrefixes.slice(0, 30));
