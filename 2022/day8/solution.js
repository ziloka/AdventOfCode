function printVisMap(visMap) {
  console.log(visMap.map(row => row.map(x => x.toString()).join('')).join('\n'));
}

function seenTrees(direction, tree) {
  for (let i = 0; i < direction.length; i++) {
      if (direction[i] >= tree) {
          return i + 1;
      }
  }
  return direction.length;
}

function solution(input) {
  const forest = input.map(x => x.split('').map(t => parseInt(t)))
  const sideLength = forest.length; 
  const visMap = forest.map(_ => new Array(sideLength).fill(1)); // if visable --> 1
  const scenic_scores = [];
  for (let row = 1; row < sideLength - 1; row++) { 
      for (let col = 1; col < sideLength - 1; col++) { /// for each tree
          const currentTree = forest[row][col];
          const top = forest.slice(0, row).map(row => row[col]);
          const bot = forest.slice(row + 1).map(row => row[col]);
          const lef = forest[row].slice(0, col);
          const rig = forest[row].slice(col + 1);
          const isInvisible = [top, bot, lef, rig].map(dir => dir.some(tree => tree >= currentTree)).every(dir => dir);
          if (isInvisible) {
              visMap[row][col] = 0;
          } else {
              const seen_top = seenTrees(top.reverse(), currentTree);
              const seen_bot = seenTrees(bot, currentTree);
              const seen_lef = seenTrees(lef.reverse(), currentTree);
              const seen_rig = seenTrees(rig, currentTree);
              const scenic_score = seen_top * seen_bot * seen_lef * seen_rig;
              scenic_scores.push(scenic_score);
          }
      }
  }
  return [visMap.reduce((a, row) => a + row.reduce((q, tree) => q + tree), 0), Math.max(...scenic_scores)];
}

const input = require('fs').readFileSync("input.txt", "utf8")
const lines = input.trim().split(/\r?\n/);
console.time();
const [answer1, answer2] = solution(lines);
console.log(`part 1: ${answer1}`);
console.log(`part 2: ${answer2}`);
console.timeEnd();
