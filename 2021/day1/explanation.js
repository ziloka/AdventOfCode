function getInput(){
    return require('fs').readFileSync('./input.txt', 'utf8');
}

function part1(arr){
  let result = 0; // result since there is no default value besides a number that is just a placeholder which is 0
  let previousValue = arr[0];
  for(let num of arr){
    if(previousValue < num) result++;
    previousValue = num;
  }
  return result;
}

function part2(arr){
  let result = 0; // the result, it starts at 0 since at the beginning there is no input
  let previousValue = arr[0]; // first value is default value
  for(let i=1;i<arr.length;i++){ // skip element at index 0 since we use that as default previous value
    let sum = arr.slice(i, i+3).reduce((a, b) => a+b); // add up the three values, return isNaN if one number is undefined
    if(isNaN(sum)) break; // check if sum is isNaN, meaning that we reached the arr.length-2 element
    if(previousValue < sum) result++; // if the previousValue is less than the sum add it to the result
    previousValue = sum; // assign sum to the previous value after doing all the logic
  }
  return result;
}

const input = getInput();
const arr = input.split("\n").map((s) => +s.trim()); /// split, and convert strings into numbers
console.time();

console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();