# A number of n coins are given, with values of a1, ..., an and a value S. 
# Display all payment modalities for the sum s. If no payment modality exists print a message.

def recursive(i : int, vals : list, s : int, used : list) -> bool:
    if s == 0:
        print(used)
        return True
    if i >= len(vals):
        return False
    sol = False
    if vals[i] <= s:
        sol |= recursive(i+1, vals, s - vals[i], used + [vals[i]])
    sol |=  recursive(i+1, vals, s, used)
    return sol 

def iterative(vals : list, s : int) -> list:
    stack = []
    stack.append((0, s, []))
    sols = []
    while stack: 
        (current_idx, current_sum, used) = stack.pop()
        if current_sum == 0:
            sols.append(used)
            continue
        if current_idx >= len(vals):
            continue
        if vals[current_idx] <= current_sum:
            stack.append((current_idx+1, current_sum - vals[current_idx], used + [vals[current_idx]]))
        stack.append((current_idx+1, current_sum, used))
    return sols

def io():
    n = int(input("n = "))
    line = input("values = ")
    tokens = line.split()
    vals = []
    for token in tokens:
        vals.append(int(token))
    s = int(input("s = "))
    ok = recursive(0, vals, s, [])
    sols = iterative(vals, s)
    if not ok:
        print("There are no solutions")
    for i in sols:
        print(i)

io()
