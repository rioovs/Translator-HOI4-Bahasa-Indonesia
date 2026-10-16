const fs = require('fs');

const p = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/equip_naval_l_english.yml';
const lines = fs.readFileSync(p, 'utf8').split(/\r?\n/);

let currentTag = 'HEADER';
let tagCount = 0;
let startLine = 1;

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  let tag = 'COMMENT_OR_BLANK';
  const m = line.match(/^\s*([A-Za-z0-9_-]+):/);
  if (m) {
    const key = m[1];
    const parts = key.split('_');
    if (parts[0].length === 3 && parts[0] === parts[0].toUpperCase()) {
      tag = parts[0];
    } else {
      tag = 'GENERIC';
    }
  }

  if (tag !== 'COMMENT_OR_BLANK') {
    if (tag !== currentTag) {
      if (tagCount > 0) {
        console.log(`Lines ${startLine}-${i}: ${currentTag} (${tagCount} keys)`);
      }
      currentTag = tag;
      startLine = i + 1;
      tagCount = 1;
    } else {
      tagCount++;
    }
  }
}
if (tagCount > 0) {
  console.log(`Lines ${startLine}-${lines.length}: ${currentTag} (${tagCount} keys)`);
}
