function getInput(){

  return require("fs").readFileSync("input.txt", "utf8")
}

function part1(arr){
let recur = (callNumbers, boards, marks,callPos) => {
// numbers that should be checked

let callNumber = callNumbers[callPos];
console.log(`calling ${callPos} for with number ${callNumber}`);
for (let boardNumber=0;boardNumber<boards.length;boardNumber++){
  // checking if nums is inside board at specified position
  let tempMark= marks[boardNumber]??[];
    for (let j=0;j<boards[boardNumber].length;j++){   
      //console.log(`${boards[boardNumber][j]}`);
      //console.log(`${boards[boardNumber][j]}`);
     tempMark[j] = tempMark[j]==true? true: callNumber==boards[boardNumber][j];    
    }
    marks[boardNumber]= tempMark;
  }

// check if a board is a winner
let boardWinner = -1;
for(let i=0;i<boards.length;i++){
  // identify board winner based off of index using markers array
  let boardMarker = marks[i];
  console.log(`Board markers: ${JSON.stringify(boardMarker) ?? 0} for board # ${i}`);
  if([0, 1, 2, 3, 4].every((e) => boardMarker[e])){ // hardcode winnable board possibilites
    boardWinner = i;
    break;      
  }else if([5,6,7,8,9].every((e) => boardMarker[e])){ // hardcode winnable board possibilites
    boardWinner = i;
    break;
  }else if([10, 11, 12, 13, 14].every((e) => boardMarker[e])){ // hardcode winnable board possibilites
    boardWinner = i;
    break;
  }else if([15, 16, 17, 18, 19].every((e) => boardMarker[e])){ // hardcode winnable board possibilites
    boardWinner = i;
    break;
  }else if([20, 21, 22, 23, 24].every((e) => boardMarker[e])){ // hardcode winnable board possibilites
    boardWinner =i;
    break;
  }else if([0, 5, 10, 15, 20].every((e) => boardMarker[e])){ // hardcode winnable board possibilites
    boardWinner = i;
    break;
  }else if([1, 6, 11, 16, 21].every((e) => boardMarker[e])){ // hardcode winnable board possibilites
    boardWinner = i;
    break;
  }else if([2, 7, 12, 17, 22].every((e) => boardMarker[e])){ // hardcode winnable board possibilites
    boardWinner = i;
    break;
  }else if([3, 8, 13, 18, 23].every((e) => boardMarker[e])){ // hardcode winnable board possibilites
    boardWinner = i;
    break;
  }else if([4, 9, 14, 19, 24].every((e) => boardMarker[e])){ // hardcode winnable board possibilites
    boardWinner = i;
    break;
  }else if([0, 6, 12, 18, 24].every((e) => boardMarker[e])){ // hardcode winnable board possibilites
    boardWinner = i;
    break;
  }else if([4, 8, 12, 16, 20].every((e) => boardMarker[e])){ // hardcode winnable board possibilites
    boardWinner = i;
    break;
  }
}

if(boardWinner >=0  ){
  console.log(`Board markers: ${JSON.stringify(boardwiner) ?? 0} for board # ${JSON.stringify(boardWinner)}`);
  console.log(`calling ${callPos} for with number ${callNumber}`);
  return boardWinner;
} 
 return recur(callNumbers, boards, marks,callPos+1);
}

let data = recur(arr[0].split(","), arr.slice(1).map((s) => s.split(/\s+/gmi)), [], 0);
console.log(data);
}

function part2(arr){
}

let arr = getInput().split("\n\n").map((s) => s.trim());
let winningPos= [0, 1, 2,3, 4];

console.time();
console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();