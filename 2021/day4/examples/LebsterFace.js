// https://github.com/LebsterFace/AdventOfCode/tree/master/solutions/day4

const input = require("fs")
	.readFileSync("../input.txt", "utf-8")
	.trim()
	.split("\n\n");

/** @type {number[]} */
const numbers = input.splice(0, 2)[0].split(",").map(Number);
/** @type {number[][][]} */
const boards = input.reduce((acc, line) => {
	if (line.length === 0) {
		acc.push([]);
	} else {
		acc[acc.length - 1].push(line.split(/\s+/).map(Number))
	}

	return acc;
}, [[]]);

let first = null;
let last = null;

for (const number of numbers) {
	boards: for (let boardNum = boards.length - 1; boardNum >= 0; boardNum--) {
		const board = boards[boardNum];
		for (const row of board) {
			let marked = null;
			for (let i = 0; i < row.length; i++) {
				if (row[i] === number) {
					row[i] = -1;
					marked = i;
				}
			}

			if (marked === null || !(
				row.every(column => column < 0) ||
				board.every(row => row[marked] < 0)
			)) continue; // If the board has not won, move to the next cell

			// Calculate the score of the board
			const score = board
				.flat()
				.filter(n => n > 0)
				.reduce((sum, current) => sum + current, 0) * number;

			if (first === null) first = score; // If the first has not been found, this is the first
			last = score; // This is also the last

			boards.splice(boardNum, 1); // Remove the current board
			continue boards; // Move to the next board
		}
	}
}

console.log("One:", first);
console.log("Two:", last);