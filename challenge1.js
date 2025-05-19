const readline = require('readline');

const terminal = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let inputLines = [];
let maxInt = 0;
let radius = 0;
terminal.on('line', (line) => {
    inputLines.push(line.trim());
    if (inputLines.length === 1) {
        maxInt =  parseInt(inputLines[0], 10);
        radius = maxInt / 2
    }
    if (inputLines.length === maxInt + 1) { // accounting for the first index being used by maxInt
        let array = inputLines.slice(1, maxInt + 1);
        let result = 0;
        for (let i = 0; i < radius; i++) {
            if (array[i] === array[i + radius]) {
                result += 2;
            }
        }

        console.log(result);
        terminal.close();
    }
});