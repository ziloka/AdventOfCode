const sections = require('fs').readFileSync("input.txt", "utf8").split("\n").map((s) => s.split(",").map((s2) => s2.split("-").map((d) => +d)));

function getPairs(func) {
  return sections.filter(([[min, max], [min2, max2]]) => func(Array.from(new Array(max - min + 1), (_, i) => i + min), Array.from(new Array(max2 - min2 + 1), (_, i) => i + min2))).length;
}

function part1() {
  return getPairs((arr, arr2) => arr.every((e) => arr2.includes(e)) || arr2.every((e) => arr.includes(e)));
}

function part2() {
  return getPairs((arr, arr2) => arr.find((e) => arr2.includes(e)) || arr2.find((e) => arr.includes(e)));
}

let start = process.hrtime.bigint();
console.log(`part 1: ${part1()}`);
console.log(`part 2: ${part2()}`);
console.log(`took: ${(process.hrtime.bigint() - start) / 1_000_000n}ms`);