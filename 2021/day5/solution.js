function getInput(){
  return require("fs").readFileSync("input.txt", "utf8");
}

function generateDiagram(arr){
  
}

function part1(arr){
  let diagram = generateDiagram(arr);
}

function part2(arr){

}

const arr = getInput().split("\n").map((a) => a.split("->").map((b) => b.trim()).map((c) => c.split(",")));

console.time();
console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();