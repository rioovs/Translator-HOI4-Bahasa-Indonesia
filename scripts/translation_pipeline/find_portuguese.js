const fs = require("fs");
const path = require("path");

const dir = "F:\\Apps\\Hearts_of_Iron_IV\\Hearts of Iron IV\\localisation\\braz_por";
const files = fs.readdirSync(dir).filter(f => f.endsWith(".yml"));

const ptWords = ["não", "você", "para", "com", "dos", "das", "governo", "guerra", "país", "divisão", "infantaria", "tropas", "pesquisa", "política", "exército", "marinha"];
const regex = new RegExp("\\b(" + ptWords.join("|") + ")\\b", "gi");

let ptCount = 0;
for (const f of files) {
  const content = fs.readFileSync(path.join(dir, f), "utf8");
  const matches = content.match(regex);
  if (matches && matches.length > 5) {
    ptCount++;
    console.log(`${f}: ${matches.length} matches (sample: ${matches.slice(0, 5).join(", ")})`);
  }
}
console.log(`\nTotal files with Portuguese matches: ${ptCount}`);
