const rucksacks = require('fs').readFileSync("input.txt", "utf8").split("\n").map((s) => s.split(""));

function getPriority(char) {
  return char == char.toUpperCase() ? char.charCodeAt(0) - 38 : char.charCodeAt(0) - 96;
}

function part1() {
  return rucksacks.reduce((a, b) => a + getPriority(b.slice(0, b.length/2).find((e) => b.slice(b.length/2).includes(e))), 0);
}

function part2() {
  let result = 0;
  for (let i = 0; i <= rucksacks.length-3; i+=3) result += getPriority(rucksacks[i].find((e) => rucksacks[i+1].includes(e) && rucksacks[i+2].includes(e)));
  return result;
}

let start = process.hrtime.bigint();
console.log(`part 1: ${part1()}`);
console.log(`part 2: ${part2()}`);
console.log(`took: ${(process.hrtime.bigint() - start) / 1_000_000n}ms`);
