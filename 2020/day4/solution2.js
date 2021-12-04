// https://www.reddit.com/r/adventofcode/comments/k6e8sw/comment/ggrc7or/?utm_source=share&utm_medium=web2x&context=3
// Source: https://tranzystorek-io.github.io/paste/#XQAAAQAGEAAAAAAAAAA9iImGVD/UQZfk+oJTfwg2/VsJ0DpNkr2zGUvTQlsh3wS86ErCiIs+8hruVNIFt25kOOZrzOGZxbRwHmJ5wrAVdOuA2kk0mNS0CwkIEqOmO95EhbRoIUTonrtGzVALDhyFMRO24/2oA0Lt4k+Q2E/wp4YaHUgbXZtC5amaE5MmewTUwYV3d2c08XNXkJSlcNdZoC0u7tg9I5cHLIpkD1dei0IndZK6Z7FBqTPLwS1LkEa4ou1cQJGg8RZJ8h2ze5RPNmVkJ8u3yi+tXn91oYB6ybzYAWHSGzz56CMhQGFOSVRb0kge7dV9wrFG6In43DAoZ+xrrdl+XSkz5iXhYhZtq4Kzyp+rFWiXolcDjjEwJQeSehZhv0qeaEVH/VD2cznO73vziSaSLFkUuJEZQpMdiJBMWEXZOUgnsEdmtMMSLexS1EGfQ0VGfv8MOJGzJ5YaxkxIgm2+iKZKJUDuU+KSP0c1FLq1lu9ylKpPqL7GFyMv+2mVtul1L4eBpBqL0oY7uYZXFNj5hrhLCFRJsLnRNtKuDvcjL/KnDueWJBBRtFJlXbEUsXOtajzjK+b+UMpw9uwYmyTD0SbGEKAaPSeA2NkfKpBJKiYlG2Ej9AQmi2PHDzNIur5sMnHwE5xfrutk8HkDXfdJQW6uToyUM6/pyXe8AoXnS/rBNcKW+cW9X8pvpGLzmv13zHFXN67P6zLXGcfEbSa8M3CtQRbo26HAu9Hf1lArQSBh+yOmhTD4rFzyoqSOStIblRcEKHmhOYJTDgfbwjKrxwKoK6vwwNvoRpiVAeaoby9XClt/70nbPxb95I6S5hgu8ufy9UIKFZLuCQZTDZ3yTOR04udmN+MM+e+vqe5xhdfinmBQvOtnjXNOD4lKZnFizw532UenIJlySKUKHyWKPTEZaf8Jj2LBpQH4+wz5Tk7kqWe2a8NV9HZ1Z0LstAPYmOhL1FTZ/nf+vsEULSy6Q6nuz/IAGB26heb7mLITZplgsmXHmanNVZnG/WduPhYHuo7Wwc5xE+uA7LN4Gy303VsAG2SnzszVcSp5HX/B2xQ6UcRZ8JQOIOfRDqUjQPQ+pEQ0Q4IoTdt9K9xcNRZZx26Sd9LtztABdrY13ssgcm4bTbarjyLmraUVOJp/F0WNq/rBdtDs2rKzLLiG6D02qYChJb658QmIJ42KtmLCyhGkQ5GmVbwid7GGIU4ToAZ5v0dEBXDw4wKHjnSrd3EJBuSNFXJfQahZlMc4f3YdPEN2930bvU/1h7XBpJ48EScB3Tc2lXXce37YDZWRLqrQk9NcGzgPVR3MxHVxekvrQqXi0Qa7lpwDzaBGkKX7LPQpX9fs3Hcf1zZbM+wZAjLLle+d1Y2wypRd52SM8Y7EyOYWHxL6mzz1MO4b9ecIgGNn5loTMgbOYQsmliK2wQJujW4x1KGyU6DhbE4v79Nbf7mPK+DdK4vbAofwd4dvaFokyskt3v4hmI3rXWnz/bhgQdlKYktRxVrqUleHOSlKDK9lRF3GRo8jFl7hVtfLo10BLOc52+YKu0F/owJ1CfLznYnk7UKq8u4Lk/9YRlPAH+j0fOdjehflu2xRAP3TgOAeRYm71NxmCOy+DZHB1yoPMWVJb7Dfa6VuOAQeqdizGUX6c69oDmXy58zxpzIL3//Z9YrG

const path = require('path');
const fs = require('fs');

const input = fs
	.readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
	.toString()
	.trim()
	.split('\n\n')
	.map((line) => {
		// Put the entries all on one line
		return line.split('\n').join(' ');
	});

const REQUIRED_FIELDS_RULES = {
	// byr (Birth Year) - four digits; at least 1920 and at most 2002.
	'byr:': {
		regex: /\bbyr:(\d+)\b/,
		extract(line) {
			let [, val] = this.regex.exec(line) || [];
			val = val ? parseInt(val) : 0;
			return val;
		},
		validate(byr) {
			return String(byr).length === 4 && byr >= 1920 && byr <= 2002;
		},
	},
	// iyr (Issue Year) - four digits; at least 2010 and at most 2020.
	'iyr:': {
		regex: /\biyr:(\d+)\b/,
		extract(line) {
			let [, val] = this.regex.exec(line) || [];
			val = val ? parseInt(val) : 0;
			return val;
		},
		validate(iyr) {
			return String(iyr).length === 4 && iyr >= 2010 && iyr <= 2020;
		},
	},
	// eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
	'eyr:': {
		regex: /\beyr:(\d+)\b/,
		extract(line) {
			let [, val] = this.regex.exec(line) || [];
			val = val ? parseInt(val) : 0;
			return val;
		},
		validate(eyr) {
			return String(eyr).length === 4 && eyr >= 2020 && eyr <= 2030;
		},
	},
	// hgt (Height) - a number followed by either cm or in:
	//     If cm, the number must be at least 150 and at most 193.
	//     If in, the number must be at least 59 and at most 76.
	'hgt:': {
		regex: /\bhgt:(\d+)(cm|in)\b/,
		extract(line) {
			let [, height, units] = this.regex.exec(line) || [];
			height = height ? parseInt(height) : 0;
			return [height, units];
		},
		validate([height, units]) {
			if (units === 'cm') {
				return height >= 150 && height <= 193;
			} else if (units === 'in') {
				return height >= 59 && height <= 76;
			} else {
				return false;
			}
		},
	},
	// hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
	'hcl:': {
		regex: /\bhcl:#([0-9a-f]+)\b/,
		extract(line) {
			let [, val = ''] = this.regex.exec(line) || [];
			return val;
		},
		validate(hcl) {
			// Regex ensures it is a hex string
			return String(hcl).length === 6;
		},
	},
	// ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
	'ecl:': {
		regex: /\becl:(amb|blu|brn|gry|grn|hzl|oth)\b/,
		extract(line) {
			let [, val = ''] = this.regex.exec(line) || [];
			return val;
		},
		validate(ecl) {
			// Regex ensures it is one of the valid colors
			return String(ecl).length === 3;
		},
	},
	// pid (Passport ID) - a nine-digit number, including leading zeroes.
	'pid:': {
		regex: /\bpid:(\d+)\b/,
		extract(line) {
			let [, val = ''] = this.regex.exec(line) || [];
			return val;
		},
		validate(pid) {
			// Regex ensures it is numbers only
			return String(pid).length === 9;
		},
	},
};
const REQUIRED_FIELDS = Object.keys(REQUIRED_FIELDS_RULES);
const REQUIRED_RULES = Object.values(REQUIRED_FIELDS_RULES);

// Part One
const includesAllRequiredFields = (entry) => {
	return REQUIRED_FIELDS.every((field) => entry.includes(field));
};

// Part Two
const allFieldsAreValid = (entry) => {
	return REQUIRED_RULES.every((rule) =>
		// Importantly, don't destructure the functions from the rule,
		// otherwise the `this` binding won't work
		rule.validate(rule.extract(entry))
	);
};

let valid_passports_p1 = input
	.map((passport) => (includesAllRequiredFields(passport) ? 1 : 0))
	.reduce((a, b) => a + b, 0);

console.log('Part One:', valid_passports_p1);

let valid_passports_p2 = input
	.filter((passport) => includesAllRequiredFields(passport))
	.map((passport) => (allFieldsAreValid(passport) ? 1 : 0))
	.reduce((a, b) => a + b, 0);

console.log('Part Two:', valid_passports_p2);