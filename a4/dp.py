# Given the set of positive integers S and the natural number k, display one of the subsets of S which sum to k. 
# For example, if S = { 2, 3, 5, 7, 8 } and k = 14, subset { 2, 5, 7 } sums to 14

def naive(vals : list, s : int) :
    for mask in range(1<<len(vals)):
        current_sum = 0
        for bit in range(len(vals)):
            if((1<<bit) & mask):
                current_sum += vals[bit]
        if current_sum == s:
            sol = []
            for bit in range(len(vals)):
                if((1<<bit) & mask):
                    sol.append(vals[bit])
            return sol
    return []

def dp(vals : list, s : int):
    dp = [[0 for _ in range(s+1)] for _ in range(len(vals))]
    prev = [[0 for _ in range(s+1)] for _ in range(len(vals))]
    dp[0][0] = 1 
    if vals[0] <= s:
        dp[0][vals[0]] = 1
    max_sum = vals[0] 
    for i in range(1, len(vals)):
        max_sum += vals[i]
        for j in range(min(s, max_sum)+1):
            if dp[i-1][j] == 1:
                dp[i][j] = 1 
                prev[i][j] = j
            if j - vals[i] >= 0 and dp[i-1][j-vals[i]] == 1:
                dp[i][j] = 1 
                prev[i][j] = j - vals[i]
    if dp[len(vals)-1][s] == 0:
        return ([], dp);
    used = []
    i = len(vals) - 1
    j = s
    while i != -1:
        if prev[i][j] != j:
            used.append(vals[i])
        j = prev[i][j]
        i -= 1
    used.reverse()
    return (used, dp);

def io():
    line = input("values = ")
    tokens = line.split()
    vals = []
    for token in tokens:
        vals.append(int(token))
    k = int(input("k = "))
    print("1 - naive solution")
    print("2 - dynamic programming solution")
    opt = int(input(" >>> "));
    if opt == 1:
        solution = naive(vals, k);
        print("The naive implementation generates all possible subsets of the values and finds one that")
        print("has the sum of its elements equal to", k)
        if len(solution):
            print(solution)
        else:
            print("Impossible")
    elif opt == 2:
        print("The dynamic programming implementation uses the matrix dp[i][j]")
        print("dp[i][j] can be either 0 or 1")
        print("dp[i][j] is 1 if it is possible to obtain the sum j from a subset of the first i values")
        (solution, matrix) = dp(vals, k)
        print()
        print("Here is the matrix dp:")
        for i in range(len(vals)):
            print(matrix[i])
        print()
        print("Solution:", solution)

io()
