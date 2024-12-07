// https://www.reddit.com/r/adventofcode/comments/k7ndux/comment/gevkhmx/?utm_source=share&utm_medium=web2x&context=3

const getInput = () => require('fs').readFileSync('./input.txt', 'utf8');

const groups = getInput().split('\n\n');
const intersect = (l, r) => new Set(
    [...l].filter(v => r.has(v))
);
Array.prototype.sumSizes = function() {
    return this.reduce((s,v) => s + v.size, 0);
}
console.log({
    part1: groups.map(
            g => new Set(g.trim().split(/\s?/))
        ).sumSizes(),

    part2: groups.map(
            g => g.trim().split('\n').map(x => new Set(x)).reduce(intersect)
        ).sumSizes()
});