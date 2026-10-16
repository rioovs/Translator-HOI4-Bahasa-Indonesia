const fs = require('fs');
const p4 = JSON.parse(fs.readFileSync('scripts/focus_part4_extracted.json', 'utf8'));

console.log('Part 4 total items:', p4.length);
console.log('First 5 items:');
p4.slice(0, 5).forEach(x => console.log(x.key, ':', x.val.substring(0, 60)));
console.log('Last 5 items:');
p4.slice(-5).forEach(x => console.log(x.key, ':', x.val.substring(0, 60)));

const prefixes = {};
p4.forEach(x => {
  const p = x.key.split('_')[0];
  prefixes[p] = (prefixes[p] || 0) + 1;
});
console.log('Part 4 prefixes:', prefixes);
