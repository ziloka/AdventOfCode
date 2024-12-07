function getInput(){
// return `00100
//         11110
//         10110
//         10111
//         10101
//         01111
//         00111
//         11100
//         10000
//         11001
//         00010
//         01010`;
    return require("fs").readFileSync("input.txt", "utf8")
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
  return parseInt(mostCommonUsedBit, 2) * parseInt(mostCommonUsedBit, 2);
}

function part2(arr){
    // determine co2Rating (most common bit)
    let co2Rating = arr.slice();
    for (let i=0;i<arr[0].length && co2Rating.length != 1;i++){ // at specified index
      let numOf1 = 0;
      let numOf0 = 0;
      for(let string of co2Rating) { // for each string
        let num = string[i]; // get string char at specified index
        if(num == 1) numOf1++;
        else numOf0++;
      }
      co2Rating = co2Rating.filter((s) => s.charAt(i) == (numOf1 < numOf0 ? "1" : "0"));
    }
    co2Rating = parseInt(co2Rating[0], 2);
    // determine oxygenGeneratorRating (least common bit)
    let oxygenGeneratorRating = arr.slice();
    for (let i=0;i<arr[0].length;i++){ // at specified index
      let numOf1 = 0;
      let numOf0 = 0;
      for(let string of oxygenGeneratorRating) { // for each string
        let num = string[i]; // get string char at specified index
        if(num == 1) numOf1++;
        else numOf0++;
      }
      oxygenGeneratorRating = oxygenGeneratorRating.filter((s) => s.charAt(i) == (numOf1 >= numOf0 ? "1" : "0"));
    }
    oxygenGeneratorRating = parseInt(oxygenGeneratorRating[0], 2);
    return co2Rating * oxygenGeneratorRating; // the life support rating
}

let arr = getInput().split("\n").map((s) => s.trim());
console.time();
console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();