const fs = require('fs');
const p2 = JSON.parse(fs.readFileSync('scripts/focus_part2_extracted.json', 'utf8'));

console.log('Part 2 total items:', p2.length);
console.log('First 5 items:');
p2.slice(0, 5).forEach(x => console.log(x.key, ':', x.val.substring(0, 60)));
console.log('Last 5 items:');
p2.slice(-5).forEach(x => console.log(x.key, ':', x.val.substring(0, 60)));

const prefixes = {};
p2.forEach(x => {
  const p = x.key.split('_')[0];
  prefixes[p] = (prefixes[p] || 0) + 1;
});
console.log('Part 2 prefixes:', prefixes);
