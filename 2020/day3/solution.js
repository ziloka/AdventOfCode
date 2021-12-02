function getInput(){
    return `..##.......
            #...#...#..
            .#....#..#.
            ..#.#...#.#
            .#...##..#.
            ..#.##.....
            .#.#.#....#
            .#........#
            #.##...#...
            #...##....#
            .#..#...#.#`;
    // return require('fs').readFileSync('./input.txt', 'utf8');
}

function part1(arr){
    let result = 0;
    let previousXValue = 0; // starting x point
    for(let i=1;i<arr.length;i++){ // on each iteration the y position gets shifted by 1
        let str = arr[i];
        previousXValue = previousXValue + 3;// the x position to check
        if(previousXValue >= str.length){ // check if we are unable to access character at specified position
            // generate longer string so we can access the char position
            let temp = "";
            for(let i=0;i<=previousXValue%str.length;i++){
                temp = temp + str;
            }
            str = temp;
        }
        // access string
        if(str.charAt(previousXValue) == "#"){ // if at specific position was a tree, # is a tree
            result++;
        }
    }
    return result;
}

function part2(arr){
    
}

const input = getInput();
const arr = input.split("\n").map((s) => s.trim()); /// split, and trim space
console.time();

console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();