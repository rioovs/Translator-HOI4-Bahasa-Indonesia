const fs = require('fs');

const descs = require('./naval_descs.json');

const uniqueMap = {};
for (const d of descs) {
  if (d.val.startsWith('$') && d.val.endsWith('$')) continue;
  if (!uniqueMap[d.val]) uniqueMap[d.val] = [];
  uniqueMap[d.val].push(d.key);
}

const uniqueList = [];
for (const [val, keys] of Object.entries(uniqueMap)) {
  uniqueList.push({ val, keys });
}

console.log('Total unique descriptions:', uniqueList.length);
fs.writeFileSync('f:/New Coding/rea-hoi4-indonesia/unique_naval_descs.json', JSON.stringify(uniqueList, null, 2), 'utf8');
console.log('Saved unique_naval_descs.json');
