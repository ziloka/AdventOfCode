const input = require('fs').readFileSync("input.txt", "utf8").split("\n").map((s) => s.split(" "));

const getFileSystem = () => {
  let directories = {};
  let dir = [''];
  for (let [a, b, c] of input) {
    if (a == "$") {
      if (b == "cd" && c == "..") dir.pop();
      else if (b == "cd") dir.push(c + '/');
    } else {
      if ((a == "$" && b == "ls") || a == "dir") continue;
      Array.from(
        { length: dir.length },
        (_, i) => dir.slice(0, i + 1).reduce((a, b) => a + b, '')
      ).forEach((p) => {
        directories[p] = (directories[p] ?? 0) + Number(a)
      });
    }
  }
  return directories;
};

let fs = getFileSystem();
console.time();
console.log(`part 1: ${Object.values(fs).filter((s) => s <= 100_000).reduce((a, b) => a+b)}`);
console.log(`part 2: ${Math.min(...Object.values(fs).filter((s) => s >= fs[''] - 40_000_000))}`);
console.timeEnd();
