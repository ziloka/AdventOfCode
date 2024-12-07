
function getInput() {
  return require("fs").readFileSync("input.txt", "utf8")
}

const arr = getInput().split("\n\n").map((s) => s.trim());
const boards = arr.slice(1).map((s) => s.split(/\s+/g).map((d) => +d));
const callNumbers = arr[0].split(",").map((d) => +d);

/**
 * Determine the winner that would win first
 * @param {number[]} marks 
 * @param {number} callPos 
 * @returns {{ index: number, board: number[], marks: number[], callNumber: number }}
 */
function getWinner(marks = [], callPos = 0) {
  let callNumber = callNumbers[callPos];
  for (let boardNumber = 0; boardNumber < boards.length; boardNumber++) {
    let tempMark = marks[boardNumber] ?? [];
    // determine is the number is on the board
    for (let j = 0; j < boards[boardNumber].length; j++) tempMark[j] = tempMark[j] ? true : callNumber == boards[boardNumber][j];
    marks[boardNumber] = tempMark;
  }

  let boardWinnerIndex = marks.findIndex((boardMarker) => {
    return [0, 1, 2, 3, 4].every((e) => boardMarker[e]) ||
      [5, 6, 7, 8, 9].every((e) => boardMarker[e]) ||
      [10, 11, 12, 13, 14].every((e) => boardMarker[e]) ||
      [15, 16, 17, 18, 19].every((e) => boardMarker[e]) ||
      [20, 21, 22, 23, 24].every((e) => boardMarker[e]) ||
      [0, 5, 10, 15, 20].every((e) => boardMarker[e]) ||
      [1, 6, 11, 16, 21].every((e) => boardMarker[e]) ||
      [2, 7, 12, 17, 22].every((e) => boardMarker[e]) ||
      [3, 8, 13, 18, 23].every((e) => boardMarker[e]) ||
      [4, 9, 14, 19, 24].every((e) => boardMarker[e]) ||
      [0, 6, 12, 18, 24].every((e) => boardMarker[e])
  });

  if (boardWinnerIndex >= 0) {
    let board = boards[boardWinnerIndex];
    let markedBoard = marks[boardWinnerIndex]
      .map((v, i) => ({ index: i, value: v }))
      .filter((e) => e.value == false)
      .map((o) => o.index);
    return {
      index: boardWinnerIndex,
      board: board.filter((_, i) => markedBoard.includes(i)),
      marks: markedBoard,
      callNumber
    };
  }
  return getWinner(marks, callPos + 1);
}

/**
 * determine the final score for the first board that would win
 * @returns {number}
 */
function part1() {
  let boardObj = getWinner();
  return boardObj.board
    .reduce((a, b) => a + b) * boardObj.callNumber;
}

/**
 * Determine the final score, of the last board that would win
 * @returns {number}
 */
function part2() {
  while (boards.length != 1) boards.splice(getWinner().index, 1);
  let wonBoard = getWinner();
  return wonBoard.board.reduce((a, b) => a + b) * wonBoard.callNumber;
}

console.time();
console.log(`part 1: ${part1()}`);
console.log(`part 2: ${part2()}`);
console.timeEnd();