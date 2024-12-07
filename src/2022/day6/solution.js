const input = require("fs").readFileSync("input.txt", "utf8").split("");

function getFirstUniqueStrIndex(length) {
  return input
    .findIndex((_, i) => 
      input
        .slice(i, i + length)
        .filter((v, i, a) => a.indexOf(v) == i).length == length
    ) + length;
}

console.time();
console.log(`part 1: ${getFirstUniqueStrIndex(4)}`);
console.log(`part 2: ${getFirstUniqueStrIndex(14)}`);
console.timeEnd();
