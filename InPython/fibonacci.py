def fib(n):
    if n <= 2:
        return 1
    
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    
    n = int(input("Enter the value of n: "))
    print(f"The {n}th fibonacci number is: {fib(n)}")