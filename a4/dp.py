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
            print(sol)
            return

def dp(vals : list, s : int):
    dp = [[0 for _ in range(s+1)] for _ in range(len(vals))]
    prev = [[0 for _ in range(s+1)] for _ in range(len(vals))]
    dp[0][0] = 1 
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
        print("Impossible")
        return
    used = []
    i = len(vals) - 1
    j = s
    while i != -1:
        if prev[i][j] != j:
            used.append(vals[i])
        j = prev[i][j]
        i -= 1
    print("Data structure used for dp variant:")
    for i in range(0, len(vals)):
        print(dp[i])
    print("dp[i][j] is 1 if it is possible to obtain sum j by using any of the first i numbers")
    used.reverse()
    print(used)
    print()

def io():
    line = input("values = ")
    tokens = line.split()
    vals = []
    for token in tokens:
        vals.append(int(token))
    k = int(input("k = "))
    dp(vals, k)
    naive(vals, k)

io()
