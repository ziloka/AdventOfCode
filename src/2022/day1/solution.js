const fs = require("fs");

const input = fs.readFileSync("input.txt", "utf8").split("\n\n").map((s) => s.split("\n").map((d) => +d)).map((arr) => arr.reduce((a, b) => a + b)).sort((a, b) => b - a);

console.log(`part 1: ${input[0]}`);
console.log(`part 2: ${input.slice(0, 3).reduce((a, b) => a + b) }`);
