# Solve the problem from the first set here
# Problem 2

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
    for p1 in range(1, x+1):
        p2 = x - p1
        if is_prime(p1) and is_prime(p2):
            return p1, p2
    return -1, -1

def io():
    n = input("n = ") 
    try:
        n = int(n)
        print(n)
        a, b = solve(n)
        if a == -1: 
            print("There are no two prime numbers that add up to n")
        else:
            print("Two prime numbers that add up to n are ", a, b)
    except ValueError:
        print("Please enter a natural number")

io()
