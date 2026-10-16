const fs = require('fs');
const p3 = JSON.parse(fs.readFileSync('scripts/focus_part3_extracted.json', 'utf8'));

console.log('Part 3 total items:', p3.length);
console.log('First 5 items:');
p3.slice(0, 5).forEach(x => console.log(x.key, ':', x.val.substring(0, 60)));
console.log('Last 5 items:');
p3.slice(-5).forEach(x => console.log(x.key, ':', x.val.substring(0, 60)));

const prefixes = {};
p3.forEach(x => {
  const p = x.key.split('_')[0];
  prefixes[p] = (prefixes[p] || 0) + 1;
});
console.log('Part 3 prefixes:', prefixes);
