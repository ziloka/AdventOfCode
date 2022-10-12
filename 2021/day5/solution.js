function getInput(){
  return require("fs").readFileSync("example.txt", "utf8");
}

function prettyPrintDiagram(arr) {
  console.log(arr.map((a) => a.join("")).join('\n'));
}

function generateDiagram(arr) {
  let numOfRows = arr[0][0][0]; // largest x value
  let numOfCols = arr[0][0][1]; // largest y value
  for (let [[x1, y1], [x2, y2]] of arr) {
    if (x1 > numOfRows) numOfRows = x1;
    if (x2 > numOfRows) numOfRows = x2;
    if (y1 > numOfCols) numOfCols = y1;
    if (y2 > numOfCols) numOfCols = y2;
  }
  // 2 dimensional array
  // https://medium.com/@wisecobbler/4-ways-to-populate-an-array-in-javascript-836952aea79f
  return new Array(numOfRows+1).fill(null).map(() => Array(numOfCols+1).fill(null).map(() => 0));
}

function part1(arr){
  let diagram = generateDiagram(arr);
  for (let [[x1, y1], [x2, y2]] of arr) {
    if (x1 == x2) { // horizontal line
      for (let i = Math.min(y1, y2); i <= Math.max(y1, y2); i++) diagram[x1][i]++;
    } else if (y1 == y2) { // vertical line
      for (let i = Math.min(x1, x2); i <= Math.max(x1, x2); i++) diagram[i][y2]++;
    }
  }

  let result = 0;
  for (let i = 0; i < diagram.length; i++) for (let j = 0; j < diagram.length; j++) if (diagram[i][j] >= 2) result++;
  return result;
}

function part2(arr){
  
}

const arr = getInput().split("\n").map((a) => a.split("->").map((b) => b.trim().split(',').map((n) => +n)));
// console.log(arr);

console.time();
console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();