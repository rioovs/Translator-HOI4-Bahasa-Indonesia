const fs = require('fs');
const p1 = JSON.parse(fs.readFileSync('scripts/focus_part1_extracted.json', 'utf8'));

let titles = 0;
let descs = 0;
let tts = 0;
let others = 0;

p1.forEach(x => {
  if (x.key.endsWith('_desc')) descs++;
  else if (x.key.endsWith('_tt')) tts++;
  else titles++;
});

console.log('Part 1 total:', p1.length);
console.log('Titles:', titles);
console.log('Descriptions:', descs);
console.log('Tooltips:', tts);
