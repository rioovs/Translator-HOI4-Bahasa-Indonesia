const fs = require('fs');
const p3 = JSON.parse(fs.readFileSync('scripts/focus_part3_extracted.json', 'utf8'));

console.log('Part 3 length:', p3.length);
for (let i = 0; i < p3.length; i += 50) {
  console.log(`\n--- Items ${i} to ${Math.min(i + 50, p3.length)} ---`);
  p3.slice(i, i + 10).forEach((x, idx) => {
    console.log(`[${i + idx}] ${x.key} :: ${x.val.substring(0, 60)}`);
  });
}
