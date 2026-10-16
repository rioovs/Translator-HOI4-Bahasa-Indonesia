const fs = require('fs');
const p2 = JSON.parse(fs.readFileSync('scripts/focus_part2_extracted.json', 'utf8'));

console.log('--- Part 2 Items ---');
p2.forEach((x, idx) => {
  console.log(`[${idx}] ${x.key} :: ${x.val.replace(/\n/g, '\\n')}`);
});
