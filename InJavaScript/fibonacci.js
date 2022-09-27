//Finds nth fibonacci number

const prompt = require("prompt-sync")(); //importing the prompt-sync as

const fib = (n) => {
    if (n <= 2) return 1;

    return fib(n-1) + fib(n-2);
}

let n = parseInt(prompt("Enter the value of n: "));
console.log(`The ${n}th fibonacci number is: ${fib(n)}`);