def fib_recursive(n):
    if (n <= 1):
        return n
    else: 
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib(n):
    if n in (0, 1):
        return 1
    if n & 1:  # if n is odd, it's faster than checking with modulo
        return fib((n+1)//2 - 1) * (2*fib((n+1)//2) - fib((n+1)//2 - 1))
    a, b = fib(n//2 - 1), fib(n//2)
    return a**2 + b**2

try:
    x = int(input("Insert an integer: "))
except ValueError:
    print("Not an integer!")
    exit(1)

print(str(x) + "° Fibonacci number = " + str(fib(x)))
