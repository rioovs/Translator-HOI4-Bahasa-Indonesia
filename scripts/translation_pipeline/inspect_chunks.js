const fs = require('fs');
const src = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/focus_l_english.yml';
const lines = fs.readFileSync(src, 'utf8').split(/\r?\n/);

let currentRange = null;
const ranges = [];

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  if (i === 0 || !line.trim()) continue;
  if (line.trim().startsWith('#')) {
    // console.log(`Comment at line ${i+1}: ${line.trim()}`);
    continue;
  }
  const colon = line.indexOf(':');
  if (colon === -1) continue;
  const key = line.substring(0, colon).trim();
  
  // determine country or category
  let cat = 'generic';
  const parts = key.split('_');
  const tag = parts[0];
  if (['GER', 'SOV', 'USA', 'ENG', 'uk', 'FRA', 'ITA', 'JAP', 'AST', 'CAN', 'RAJ', 'SAF', 'NZL', 'HUN', 'ROM', 'YUG', 'CZE', 'POL', 'CHI', 'PRC', 'MAN'].includes(tag)) {
    cat = tag;
  } else if (key.startsWith('continuous_')) {
    cat = 'continuous';
  } else if (key.startsWith('ah_')) {
    cat = 'ah';
  }
  
  if (!currentRange || currentRange.cat !== cat) {
    if (currentRange) {
      currentRange.endLine = i;
      ranges.push(currentRange);
    }
    currentRange = { cat, startLine: i + 1, count: 1 };
  } else {
    currentRange.count++;
  }
}
if (currentRange) {
  currentRange.endLine = lines.length;
  ranges.push(currentRange);
}

for (const r of ranges) {
  console.log(`Lines ${r.startLine}-${r.endLine} [${r.cat}]: ${r.count} keys`);
}
