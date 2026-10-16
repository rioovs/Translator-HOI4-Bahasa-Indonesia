const fs = require('fs');

const uniqueDescs = require('./unique_naval_descs.json');
console.log('Total unique descs:', uniqueDescs.length);

const chunks = [
  [0, 60],
  [60, 120],
  [120, 180],
  [180, 240],
  [240, 300],
  [300, 360],
  [360, uniqueDescs.length]
];

chunks.forEach(([start, end], idx) => {
  const chunk = uniqueDescs.slice(start, end);
  const fileName = `f:/New Coding/rea-hoi4-indonesia/chunk_${idx + 1}.json`;
  fs.writeFileSync(fileName, JSON.stringify(chunk, null, 2), 'utf8');
  console.log(`Chunk ${idx + 1} (${start}..${end}): ${chunk.length} descs saved to ${fileName}`);
});
