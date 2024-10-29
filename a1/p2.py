# Solve the problem from the second set here
# Problem 7

from math import sqrt

def is_prime(x):
    if x < 2: 
        return False
    if x == 2: 
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def solve(x):
    p1 = x + 1
    while is_prime(p1) == False or is_prime(p1 + 2) == False:
        p1 += 1
    return p1, p1 + 2

def io():
    n = input("n = ")
    try:
        n = int(n)
        a, b = solve(n)
        print("The twin prime numbers immediately larger than n are ", a, b);
    except ValueError:
        print("Please enter a natural number")

io()
