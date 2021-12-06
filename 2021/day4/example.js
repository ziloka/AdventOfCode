// Example Solution

function getInput() {
  return `7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19

3 15  0  2 22
9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7`;
  //return require("fs").readFileSync("input.txt", "utf8")
}

function part1(arr) {
  // identify board that would win first0
  let recur = (callNumbers, boards, marks, callPos) => {
    // numbers that should be checked

    let callNumber = callNumbers[callPos];
    for (let boardNumber = 0; boardNumber < boards.length; boardNumber++) {
      // checking if nums is inside board at specified position
      let tempMark = marks[boardNumber] ?? [];
      for (let j = 0; j < boards[boardNumber].length; j++) {
        tempMark[j] = tempMark[j] == true ? true : callNumber == boards[boardNumber][j];
      }
      marks[boardNumber] = tempMark;
    }

    // check if a board is a winner
    let boardWinnerIndex = -1;
    for (let i = 0; i < boards.length; i++) {
      // identify board winner based off of index using markers array
      let boardMarker = marks[i];
      if(
        [0, 1, 2, 3, 4].every((e) => boardMarker[e]) ||
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
        // [0, 6, 12, 18, 24].every((e) => boardMarker[e]) ||
        // [4, 8, 12, 16, 20].every((e) => boardMarker[e])
      ){
        boardWinnerIndex = i;
        break;
      }
    }
    if (boardWinnerIndex >=0) {
      let board = boards[boardWinnerIndex];
      let markedBoard = marks[boardWinnerIndex].map((v, i) => ({ index: i, value: v})).filter((e) => e.value == false).map((o) => o.index);

      return board.filter((_, i) => markedBoard.includes(i)).reduce((a, b) => (+a)+(+b)) * callNumber;
    }
    return recur(callNumbers, boards, marks, callPos + 1);
  }
  return recur(arr[0].split(","), arr.slice(1).map((s) => s.split(/\s+/gmi)), [], 0);
}

function part2(arr) {
  // identify board that would win last
  let recur = (callNumbers, boards, marks, callPos, lastWinner) => {
    // numbers that should be checked
    let callNumber = callNumbers[callPos];
    var lastWinnerPostions = lastWinner.map((v) => v.boardWinner);
    for (let boardNumber = 0; boardNumber < boards.length; boardNumber++) {
      // checking if nums is inside board at specified position
    var lastWinnerPostions = lastWinner.map((v) => v.boardWinner);
      if (!lastWinnerPostions.includes(boardNumber)) {
      let tempMark = marks[boardNumber] ?? [];
      for (let j = 0; j < boards[boardNumber].length; j++) {
        tempMark[j] = tempMark[j] == true ? true : callNumber == boards[boardNumber][j];
      }
      marks[boardNumber] = tempMark;} 
    }

    // check if a board is a winner
    let boardWinner = -1;
    for (let i = 0; i < boards.length; i++) {
      // identify board winner based off of index using markers array
      let boardMarker = marks[i];
       //if (i== 65) console.log(boardMarker);

      if (!lastWinnerPostions.includes(i) && (
        [0, 1, 2, 3, 4].every((e) => boardMarker[e]) ||
        [5, 6, 7, 8, 9].every((e) => boardMarker[e]) ||
        [10, 11, 12, 13, 14].every((e) => boardMarker[e]) ||
        [15, 16, 17, 18, 19].every((e) => boardMarker[e]) ||
        [20, 21, 22, 23, 24].every((e) => boardMarker[e]) ||
        [0, 5, 10, 15, 20].every((e) => boardMarker[e]) ||
        [1, 6, 11, 16, 21].every((e) => boardMarker[e]) ||
        [2, 7, 12, 17, 22].every((e) => boardMarker[e]) ||
        [3, 8, 13, 18, 23].every((e) => boardMarker[e]) ||
        [4, 9, 14, 19, 24].every((e) => boardMarker[e]) ||
        [0, 6, 12, 18, 24].every((e) => boardMarker[e]))
      ) { // hardcode winnable board possibilites
        console.log(i);
        boardWinner = i;
        break;
      } 
    }
    if (boardWinner >=0) {
      lastWinner.push({boardWinner, callNumber});
      console.log(lastWinner);
      //boards.splice(lastWinner, 1);
    }

    if(callPos == callNumbers.length-1){
      let boardWinnerIndex = lastWinner[lastWinner.length-1].boardWinner;
      let board = boards[boardWinnerIndex];
      console.log(boardWinnerIndex);
      console.log(marks);
      let markedBoard = marks[boardWinnerIndex].map((v, i) => ({ index: i, value: v})).filter((e) => e.value == false).map((o) => o.index);
      return board.filter((_, i) => markedBoard.includes(i)).reduce((a, b) => (+a)+(+b)) * lastWinner[lastWinner.length-1].callNumber; // exit 
      return lastWinner;
    }
    return recur(callNumbers, boards, marks, callPos + 1, lastWinner);
  }
  return recur(arr[0].split(","), arr.slice(1).map((s) => s.split(/\s+/gmi)), [], 0, []);
}

let arr = getInput().split("\n\n").map((s) => s.trim());

console.time();
// console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();