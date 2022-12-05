let [boxes, ...moves] = require('fs').readFileSync('input.txt', 'utf8').split('move');

// example input
// boxes = [
//   ["N", "Z"],
//   ["D", "C", "M"],
//   ["P"]
// ];

// real input
boxes = [
  ['T', 'V', 'J', 'W', 'N', 'R', 'M', 'S'], // 1
  ['V', 'C', 'P', 'Q', 'J', 'D', 'W', 'B'], // 2
  ['P', 'R', 'D', 'H', 'F', 'J', 'B'], // 3
  ['D', 'N', 'M', 'B', 'P', 'R', 'F'], // 4
  ['B', 'T', 'P', 'R', 'V', 'H'], // 5
  ['T', 'P', 'B', 'C'], // 6
  ['L', 'P', 'R', 'J', 'B'], // 7
  ['W', 'B', 'Z', 'T', 'L', 'S', 'C', 'N'], // 8
  ['G', 'S', 'L'], // 9
];

moves = moves.map((s) => {
  const [numOfBoxes, from, to] = s.match(/\d+/g).map((d) => +d);
  return {
    boxes: numOfBoxes,
    from,
    to,
  };
});

function part1(boxes) {
  for (const move of moves) {
    for (let i = 0; i < move.boxes; i += 1) { // move each box one by one
      boxes[move.to - 1].splice(0, 0, boxes[move.from - 1][0]); // append the value at the beginning of the array
      boxes[move.from - 1].splice(0, 1); // delete previous value
    }
  }
  return boxes.reduce((previousValue, currentValue) => previousValue + currentValue.find((e) => e != null), '');
}

function part2(boxes) {
  for (const move of moves) {
    boxes[move.to - 1].splice(0, 0, ...boxes[move.from - 1].slice(0, move.boxes)); // append the values at the beginning of the array
    boxes[move.from - 1].splice(0, move.boxes);
  }
  return boxes.reduce((previousValue, currentValue) => previousValue + currentValue.find((e) => e != null), '');
}

// DEEP CLONE VALUES (structuredClone method or JSON.parse(JSON.stringify(data))) because arrays are passed by reference *
console.time();
console.log(`part 1: ${part1(structuredClone(boxes))}`);
console.log(`part 2: ${part2(structuredClone(boxes))}`);
console.timeEnd();