const fs = require("fs");
const path = require("path");

const dir = "F:\\Apps\\Hearts_of_Iron_IV\\Hearts of Iron IV\\localisation\\braz_por";
const files = fs.readdirSync(dir).filter(f => f.endsWith(".yml"));

const ptWords = [" não ", " você ", " para ", " com ", " dos ", " das ", " um ", " uma ", " governo ", " guerra ", " país ", " divisão ", " infantaria ", " apoio "];
const idWords = [" tidak ", " anda ", " untuk ", " dengan ", " dari ", " dan ", " yang ", " divisi ", " angkatan ", " pemerintah ", " perang ", " negara "];

let ptCount = 0;
let idCount = 0;
let enCount = 0;

const ptFiles = [];
const idFiles = [];
const enFiles = [];

for (const f of files) {
  const content = fs.readFileSync(path.join(dir, f), "utf8").toLowerCase();
  let ptHits = 0;
  for (const w of ptWords) {
    if (content.includes(w)) ptHits++;
  }
  let idHits = 0;
  for (const w of idWords) {
    if (content.includes(w)) idHits++;
  }
  
  if (idHits > ptHits && idHits > 2) {
    idCount++;
    idFiles.push(f);
  } else if (ptHits > 2) {
    ptCount++;
    ptFiles.push({ file: f, hits: ptHits });
  } else {
    enCount++;
    enFiles.push(f);
  }
}

console.log(`Total files: ${files.length}`);
console.log(`Indonesian files: ${idCount}`);
console.log(`Portuguese files: ${ptCount}`);
console.log(`English files: ${enCount}`);

console.log("\nTop Portuguese files remaining:");
ptFiles.sort((a,b) => b.hits - a.hits).slice(0, 30).forEach(x => console.log(`  ${x.file} (${x.hits} hits)`));
