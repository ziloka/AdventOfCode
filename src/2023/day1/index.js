const fs = require("fs");
const input = fs.readFileSync("input.txt", "utf8").trim().split("\n");
const dict = { one: "1", two: "2", three: "3", four: "4", five: "5", six: "6", seven: "7", eight: "8", nine: "9" };

// regular expression solutions
const answerpart1 = input.map((s) => {
    const arr = s.match(/\d/g);
    const {0: first, [arr.length-1]: last} = arr;
    return first + last;
}).reduce((a, b) => (+a)+(+b));

// edge case: twodzbplxm9xlgvnmfvxh7oneightzvm
const answerpart2 = input.map((s) => {
    const arr = [...s.matchAll(/(?=(\d|one|two|three|four|five|six|seven|eight|nine))/g)].map((e) => e[e.length-1]);
    const {0: first, [arr.length-1]: last} = arr;
    const convert = (e) => isNaN(e) ? dict[e] : e;
    return +(convert(first) + convert(last));
}).reduce((a, b) => a+b);

// 54251 is too high
console.log(`part 1: ${answerpart1}`);
console.log(`part 2: ${answerpart2}`);

// no regular expression solutions
const nums = Object.values(dict);
const words = Object.keys(dict);

// console.log(first, last)    

const part1 = input.map((s) => {
    // const first = combo.find((e) => s.includes(e));
    // const last = combo.findLast((e) => s.includes(e));
    const arr = s.split("").filter((e) => !isNaN(e));
    const {0: first, [arr.length-1]: last} = arr;
    return +(first + last);
}).reduce((a, b) => a+b);

// const combo = nums.concat(words);
// const part2 = input.map((s) => {
//     // const first = combo.find((e) => s.includes(e));
//     // const last = combo.findLast((e) => s.includes(e));
//     // console.log(first, last)
//     const arr = s.filter((e) => !isNaN(e));
//     const {0: first, [arr.length-1]: last} = arr;
//     return first + last;
// }).reduce((a, b) => (+a)+(+b));

// console.log(part1);
// console.log(part2);
// 

