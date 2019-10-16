def fibonacci(n):
    if (n <= 1):
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

try:
    x = int(input("Insert an integer: "))
except ValueError:
    print("Not an integer!")
    exit(1)

print(str(x) + "° Fibonacci number = " + str(fibonacci(x)))
