function getInput() {
  // return `..##.......
  //         #...#...#..
  //         .#....#..#.
  //         ..#.#...#.#
  //         .#...##..#.
  //         ..#.##.....
  //         .#.#.#....#
  //         .#........#
  //         #.##...#...
  //         #...##....#
  //         .#..#...#.#`;
  return require('fs').readFileSync('./input.txt', 'utf8');
}

function part1(arr) {
  let result = 0;
  let previousXValue = 0; // starting x point
  for (let i = 1; i < arr.length; i++) { // on each iteration the y position gets shifted by 1
    let str = arr[i];
    previousXValue += 3;// the x position to check
    if (previousXValue >= str.length) { // check if we are unable to access character at specified position
      // generate longer string so we can access the char position
      let temp = "";
      for (let i = 0; i <= Math.ceil(previousXValue / str.length); i++) { // identify least amount of iterations in order to access char position
        temp += str;
      }
      str = temp;
    }
    // access string
    if (str.charAt(previousXValue) == "#") { // if at specific position was a tree, # is a tree
      result++;
    }
  }
  return result;
}

function part2(arr) {
  let result = 1;
  let slopes = [
    {
      r: 1, d: 1
    }, {
      r: 3, d: 1
    }, {
      r: 5, d: 1
    }, {
      r: 7, d: 1
    }, {
      r: 1, d: 2
    }
  ];
  // foreach slope
  for (let slope of slopes) {
    let slopeResult = 0;
    let previousXValue = 0; // starting x point
    for (let i = slope.d; i < arr.length; i += slope.d) { // on each iteration the y position gets shifted by 1
      let str = arr[i];
      previousXValue += slope.r; // the x position to check
      if (previousXValue >= str.length) { // check if we are unable to access character at scified position
        // generate longer string so we can access the char position
        let temp = "";
        for (let i = 0; i <= Math.ceil(previousXValue / str.length); i++) { // identify least amount of iterations in order to access char position
          temp += str;
        }
        str = temp;
      }
      // access string
      if (str.charAt(previousXValue) == "#") { // if at specific position was a tree, # is a tree
        slopeResult++;
      }
    }
    result = result * (slopeResult ?? 1);
  }
  return result;
}

const arr = getInput().split("\n").map((s) => s.trim()); /// split, and trim space
console.time();

console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();