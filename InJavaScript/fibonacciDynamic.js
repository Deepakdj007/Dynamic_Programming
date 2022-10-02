//Find nth fibonacci number using Dynamic programming
//Time complexity is O(n)
const prompt = require("prompt-sync")(); //importing the prompt-sync as



const fib = (n, memo = {}) =>{
    if(n in memo) return memo[n];
    if(n<=2) return 1;
    memo[n] = fib(n-1,memo) + fib(n-2,memo);
    return memo[n]
}

let n = parseInt(prompt("Enter the value of n: "));
console.log(`The ${n}th fibonacci number is: ${fib(n)}`);
