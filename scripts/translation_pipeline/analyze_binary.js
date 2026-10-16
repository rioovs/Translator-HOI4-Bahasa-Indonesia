const fs = require("fs");

const exePath = "F:\\Apps\\Hearts_of_Iron_IV\\Hearts of Iron IV\\hoi4.exe";
console.log("Reading binary:", exePath);
const buf = fs.readFileSync(exePath);
console.log("Binary size:", (buf.length / (1024 * 1024)).toFixed(2), "MB");

const targets = [
  "languages.yml",
  "l_english",
  "l_braz_por",
  "l_german",
  "l_french",
  "l_spanish",
  "l_polish",
  "l_russian",
  "l_japanese",
  "l_simp_chinese",
  "l_korean",
  "l_indonesian",
  "localisation",
  "settings.txt"
];

for (const t of targets) {
  let count = 0;
  let idx = -1;
  const positions = [];
  while ((idx = buf.indexOf(t, idx + 1)) !== -1) {
    count++;
    if (positions.length < 5) positions.push("0x" + idx.toString(16));
  }
  console.log(`Target "${t}": ${count} matches${positions.length ? " at [" + positions.join(", ") + "]" : ""}`);
}

// Find strings around languages.yml
let langIdx = buf.indexOf("languages.yml");
if (langIdx !== -1) {
  const start = Math.max(0, langIdx - 200);
  const end = Math.min(buf.length, langIdx + 300);
  console.log("\nContext around languages.yml:");
  const slice = buf.subarray(start, end).toString("binary");
  console.log(slice.replace(/[^\x20-\x7E\r\n]/g, "."));
}

// Check where language names are defined
let brazIdx = buf.indexOf("l_braz_por");
if (brazIdx !== -1) {
  const start = Math.max(0, brazIdx - 200);
  const end = Math.min(buf.length, brazIdx + 300);
  console.log("\nContext around l_braz_por:");
  const slice = buf.subarray(start, end).toString("binary");
  console.log(slice.replace(/[^\x20-\x7E\r\n]/g, "."));
}
