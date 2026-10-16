const fs = require("fs");

let script = fs.readFileSync("C:\\Users\\riook\\.gemini\\antigravity\\brain\\6e58792b-17be-450e-96fb-2abecad8ae10\\scratch\\translate_loading_tips.js", "utf8");
// replace the regex bug in the original script
script = script.replace("/\\\\r?\\\\n/", "/\\r?\\n/");
script = script.replace("/^(\\\\s*)([A-Za-z0-9_]+):\\\\s*\\\"(.*)\\\"\\\\s*$/", "/^(\\s*)([A-Za-z0-9_]+):\\s*\"(.*)\"\\s*$/");

fs.writeFileSync("f:\\New Coding\\rea-hoi4-indonesia\\scripts\\run_loading.js", script);
console.log("Patched script saved!");
