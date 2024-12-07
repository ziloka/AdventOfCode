const input = require('fs').readFileSync('input.txt', 'utf8').split(/\r?\n/).map((s) => {
  let [ p1, p2 ] = s.split(' ');
  return [ p1, +p2 ];
});

function dirToNum(dir) {
  switch (dir) {
    case 'R':
      return [1, 0];
    case 'L':
      return [-1, 0];
    case 'U':
      return [0, 1];
    case 'D':
      return [0, -1];
  }
}

function move_tail(head_cords, tail_cords, change) {
  let former_location = [tail_cords[0], tail_cords[1]];

  if (Math.abs(tail_cords[0] - head_cords[0]) > 1 || Math.abs(tail_cords[1] - head_cords[1]) > 1) {
    if (change[0] !== 0 && change[1] !== 0) {
      if (tail_cords[0] == head_cords[0]) {
        tail_cords[1] += change[1];
      } else if (tail_cords[1] == head_cords[1]) {
        tail_cords[0] += change[0];
      } else {
        tail_cords[0] += change[0];
        tail_cords[1] += change[1];
      }
    } else {
      tail_cords[0] += change[0];
      tail_cords[1] += change[1];

      if (change[0] !== 0 && tail_cords[1] !== head_cords[1]) {
        tail_cords[1] = head_cords[1];
      } else if (change[1] !== 0 && tail_cords[0] !== head_cords[0]) {
        tail_cords[0] = head_cords[0];
      }
    }
  }

  return [tail_cords[0] - former_location[0], tail_cords[1] - former_location[1]];
}

function solution(input, num_of_ropes) {
  let cords = new Set();

  let rope_cords = Array.from({ length: num_of_ropes }, (_, i) => [0, 0]);

  cords.add([...rope_cords[rope_cords.length-1]])

  for (let instr of input) {
    let dir_ = instr[0];
    for (let i = 0; i < instr[1]; i++) {
      let change = dirToNum(dir_);

      rope_cords[0][0] += change[0];
      rope_cords[0][1] += change[1];

      for (let j = 1; j < num_of_ropes; j++) {
        change = move_tail(rope_cords[j - 1], rope_cords[j], change);
        if (change[0] == 0 && change[1] == 0) break;
      }
      cords.add([...rope_cords[rope_cords.length-1]])
    }
  }
  // https://www.kirupa.com/javascript/removing_duplicate_arrays_from_array.htm
  return Array.from(new Set([...cords].map(JSON.stringify)), JSON.parse).length;
}

console.log(solution(input, 2));
console.log(solution(input, 10));