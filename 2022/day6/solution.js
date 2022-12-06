const input = require("fs").readFileSync("input.txt", "utf8").split("");

function getFirstUniqueStrIndex(length) {
  // return input.findIndex((v, i) => [...new Set(input.slice(i, i + length))].length == length) + length;
  return input
    .findIndex((_, i) => 
      input
        .slice(i, i + length)
        .filter((v, i, a) => a.indexOf(v) == i).length == length
    ) + length;
}

function part1() {
  return getFirstUniqueStrIndex(4);
}

function part2() {
  return getFirstUniqueStrIndex(14);
}

console.time();
console.log(`part 1: ${part1()}`);
console.log(`part 2: ${part2()}`);
console.timeEnd();
