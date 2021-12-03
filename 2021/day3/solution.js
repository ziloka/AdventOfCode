function getInput(){
return `00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010`;
    // return require("fs").readFileSync("input.txt", "utf8")
}

function getBinaryDiagnostic(arr){
}

function part1(arr){
    let mostCommonUsedBit = ""; // binary number in a string
    let leastCommonUsedBit = ""; // binary number in a string
    for (let i=0;i<arr[0].length;i++) { // specified index
        let numOf1 = 0;
        let numOf0 = 0;
        for(let string of arr) { // for each string
            let num = string[i]; // get string char at specified index
            if(num == 1) numOf1++;
            else numOf0++;
        }
        if(numOf1 > numOf0){
            mostCommonUsedBit = mostCommonUsedBit + "1";
            leastCommonUsedBit = leastCommonUsedBit + "0";
        } else {
            mostCommonUsedBit = mostCommonUsedBit + "0";
            leastCommonUsedBit = leastCommonUsedBit + "1";
        }
    }
    return parseInt(mostCommonUsedBit, 2) * parseInt(leastCommonUsedBit, 2);
}

function part2(arr){
    let oxygenGeneratorRating = 0; // determine using most common value
    let co2Rating = 0; // determine using least common value
    let mostCommonUsedBit = ""; // binary number in a string
    let leastCommonUsedBit = ""; // binary number in a string
    for (let i=0;i<arr[0].length;i++) { // specified index
        let numOf1 = 0;
        let numOf0 = 0;
        for(let string of arr.slice(1)) { // for each string
            let num = string[i]; // get string char at specified index
            if(num == 1) numOf1++;
            else numOf0++;
        }
        if(numOf1 > numOf0){
            mostCommonUsedBit = mostCommonUsedBit + "1";
            leastCommonUsedBit = leastCommonUsedBit + "0";
        } else {
            mostCommonUsedBit = mostCommonUsedBit + "0";
            leastCommonUsedBit = leastCommonUsedBit + "1";
        }
    }

    // determine co2Rating
    co2Rating = parseInt(mostCommonUsedBit, 2);
    // determine oxygenGeneratorRating
    oxygenGeneratorRating = parseInt(leastCommonUsedBit, 2)

    console.log(`Oxygen Generator Rating: ${oxygenGeneratorRating}, ${leastCommonUsedBit}`);
    console.log(`Co2 Rating: ${co2Rating}, ${mostCommonUsedBit}`);
    return co2Rating * oxygenGeneratorRating; // the life support rating
}

let arr = getInput().split("\n").map((s) => s.trim());
console.time();
console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();

// function getInput(){
//     return `00100
//             11110
//             10110
//             10111
//             10101
//             01111
//             00111
//             11100
//             10000
//             11001
//             00010
//             01010`;
//     // return require('fs').readFileSync('./input.txt', 'utf8');
// }

// function part1(arr){
//     let resultArr = [];
//     let gammaRay = "";
//     // build binary strings
//     for(let i=0;i<arr[0].length;i++){ // for each string
//         let numOf1 = 0;
//         let numOf0 = 0;
//         for(let string of arr){
//             if(string.charAt(i) == "1") numOf1++;
//             else numOf0++;
//         }
//         if(numOf1 > numOf0) gammaRay = gammaRay + numOf1;
//         else gammaRay = gammaRay + numOf0;
//     }
//     console.log(resultArr);
//     // return result;
// }

// function part2(arr){
   
// }

// const input = getInput();
// const arr = input.split("\n").map((s) => s.trim()); /// split, and trim space
// console.time();

// console.log(`part 1: ${part1(arr)}`);
// console.log(`part 2: ${part2(arr)}`);
// console.timeEnd();