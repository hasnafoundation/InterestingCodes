import math
import time
def fact(n): 
  if (n == 0): 
    return 1 
  else: 
    n = n * fact(n-1)
    return n

def super_fast_factorial(n):
    return math.factorial(x)

try:
    x = int(input("Insert an integer: "))
except ValueError:
    print("Not an integer")

start_fast = time.time()
print(str(x) + "! = " + str(super_fast_factorial(x)))
stop_fast = time.time()
time_fast = stop_fast - start_fast
print("Time elapsed (fast function): " + str(time_fast)) 

try:
    start_recursive = time.time()
    stop_recursive = time.time()
    time_recursive = stop_recursive - start_recursive
    print(str(x) + "! = " + str(fact(x)))
except RecursionError:
    print("Maximum recursion depth exceeded")
    time_recursive = math.inf
print("Time elapsed (recursive function): " + str(time_recursive))

print("Fast function is " + str(time_recursive/time_fast) + " times faster than recursive function")

