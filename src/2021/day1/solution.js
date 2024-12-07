const arr = require('fs').readFileSync('./input.txt', 'utf8').split("\n").map((s) => +s.trim());
console.time();
let part1 = 0;
let part2 = 0;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
let part1PreviousValue = arr[0];
let part2PreviousValue = arr[0];
for(let i=0;i<arr.length-1;i++){
  // part 1
  if(part1PreviousValue < arr[i]) part1++;
  part1PreviousValue = arr[i];

  // part 2
  let sum = arr.slice(i+1, i+4).reduce((a, b) => a+b);
  if(!isNaN(sum) && part2PreviousValue < sum) {
    part2++;
  }
  part2PreviousValue = sum;
}

console.log(`part 1: ${part1}`);
console.log(`part 2: ${part2}`);
console.timeEnd();