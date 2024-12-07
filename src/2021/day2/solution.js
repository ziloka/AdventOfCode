function getInput(){
    return require('fs').readFileSync('./input.txt', 'utf8');
}

function part1(arr){
    let horizontal = 0;
    let depth = 0;
    for(let element of arr){
        let obj = element.split(" ");
        let type = obj[0];
        let num = +obj[1]; // the plus infront of it casts string into a number
        if(type == "forward"){
            horizontal = horizontal + num;
        } else if(type == "up"){
            depth = depth - num;
        } else if(type == "down"){
            depth = depth + num;
        }
    }
    return horizontal * depth;
}

function part2(arr){
    let horizontal = 0;
    let depth = 0;
    let aim = 0;
    for(let element of arr){
        let obj = element.split(" ");
        let type = obj[0];
        let num = +obj[1]; // the plus infront of it casts string into a number
        if(type == "forward"){
            horizontal = horizontal + num;
            depth = depth + (aim * num);
        } else if(type == "up"){
            aim = aim - num;
        } else if(type == "down"){
            aim = aim + num;
        }
    }
    return horizontal * depth;
}

const input = getInput();
const arr = input.split("\n").map((s) => s.trim()).filter((e) => e.length != 0); /// split, and convert strings into numbers
console.time();

console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);

console.timeEnd();