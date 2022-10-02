#Find nth fibonacci number using Dynamic programming
#Time complexity is O(n)

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    
    return memo[n]

if __name__ == '__main__':
    
    n = int(input("Enter the value of n:"))
    print(f"The {n}th fibonacci number is {fib(n)}")