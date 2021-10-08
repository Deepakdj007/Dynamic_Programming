def findFib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return(findFib(n-1) + findFib(n-2))
    

if __name__ == "__main__":

    n = int(input("Enter the fibonacci number you want to find: "))
    print(f"The {n}th fibonacci number is: {findFib(n)}")