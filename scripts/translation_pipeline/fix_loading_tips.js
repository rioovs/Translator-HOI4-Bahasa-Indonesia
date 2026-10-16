const fs = require("fs");

const script = fs.readFileSync("C:\\Users\\riook\\.gemini\\antigravity\\brain\\6e58792b-17be-450e-96fb-2abecad8ae10\\scratch\\translate_loading_tips.js", "utf8");
const start = script.indexOf("const tips = {");
const end = script.indexOf("const srcPath =");
eval(script.substring(start, end));

const srcPath = "F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/loading_tips_l_english.yml";
const targetPath = "f:/New Coding/rea-hoi4-indonesia/localisation/braz_por/loading_tips_l_braz_por.yml";
const srcContent = fs.readFileSync(srcPath, "utf8");
const lines = srcContent.split(/\r?\n/);
const outLines = ["l_braz_por:"];
let count = 0;
for (let i = 1; i < lines.length; i++) {
  const line = lines[i];
  const m = line.match(/^(\s*)([A-Za-z0-9_]+):\s*"(.*)"\s*$/);
  if (m) {
    const key = m[2];
    if (tips[key]) {
      outLines.push(`${m[1]}${key}: "${tips[key]}"`);
      count++;
    } else {
      outLines.push(line);
    }
  } else {
    outLines.push(line);
  }
}
const bom = Buffer.from([0xEF, 0xBB, 0xBF]);
const fullBuf = Buffer.concat([bom, Buffer.from(outLines.join("\r\n"), "utf8")]);
fs.writeFileSync(targetPath, fullBuf);
console.log(`Success! Translated ${count} tips, wrote ${fullBuf.length} bytes to ${targetPath}`);
