const { FORMERR } = require('dns');
const fs = require('fs')
const readline = require('readline');

inputLines = fs.readFileSync('input.txt', 'utf-8').split('\n')

for (const line of inputLines) {
    console.log(line)
}

