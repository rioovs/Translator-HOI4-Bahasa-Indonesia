const fs = require('fs');
const p1 = JSON.parse(fs.readFileSync('scripts/focus_part1_extracted.json', 'utf8'));

for (let i = 100; i < 200; i++) {
  const it = p1[i];
  console.log(`[${i}] ${it.key}: ${JSON.stringify(it.val)}`);
}
