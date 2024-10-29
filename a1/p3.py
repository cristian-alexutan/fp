# Solve the problem from the third set here
# Problem 13

def prime_divisors(n, x):
    d = 2
    ans = -1

    if x == 1:
        n -= 1
        if n == 0: 
            ans = 1
        return n, ans

    while x != 1:
        if x % d == 0:
            n -= 1
            if n == 0:
                ans = d
        while x % d == 0:
            x /= d
        d += 1
    return n, ans

def solve(n):
    i = 1
    while n > 0:
        n, sol = prime_divisors(n, i)
        i += 1
    return sol

def io():
    n = input("n = ")
    try:
        n = int(n)
        sol = solve(n)
        print("The n-th element of the sequence is ", sol)
    except ValueError:
        print("Please insert a natural number")

io()
