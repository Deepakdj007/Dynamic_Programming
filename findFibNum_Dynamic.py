def findFib(n, memo = {}):
    if n in memo:
        return memo[n]
    elif n == 0:
        memo[n] = 0
        return 0
    elif n <= 2:
        memo[n] = 1
        return 1
    else:
        fib_value = findFib(n-1) + findFib(n-2)
        memo[n] = fib_value
        return fib_value
    

if __name__ == "__main__":

    n = int(input("Enter the fibonacci number you want to find: "))
    print(f"The {n}th fibonacci number is: {findFib(n)}")