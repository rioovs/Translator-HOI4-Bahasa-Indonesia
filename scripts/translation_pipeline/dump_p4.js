const fs = require('fs');
const p4 = JSON.parse(fs.readFileSync('scripts/focus_part4_extracted.json', 'utf8'));

console.log('Part 4 length:', p4.length);
p4.forEach((x, idx) => {
  console.log(`[${idx}] ${x.key} :: ${x.val.substring(0, 60)}`);
});
