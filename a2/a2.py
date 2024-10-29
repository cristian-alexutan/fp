import os
import random
import math

def generate_list(length : int) -> list:
    v = []
    for i in range(length):
        v.append(random.randrange(0, 1000))
    return v

def exponential_search(v : list, x : int) -> tuple[int, int]: 
    exp = 1
    while (1<<exp) < len(v) and v[(1<<exp)] <= x:
        exp += 1
    pos1 = -1
    pos2 = -1
    for p in range(exp, -1, -1):
        if pos1 + (1<<p) < len(v) and v[pos1 + (1<<p)] < x:
            pos1 += (1<<p)
        if pos2 + (1<<p) < len(v) and v[pos2 + (1<<p)] <= x:
            pos2 += (1<<p)
    return pos1 + 1, pos2

def ok(st : list, k : int) -> bool:
    for i in range(0, k):
        if st[i] == st[k]: 
            return False
    return True

def ascending(pos : int, v : list) -> bool:
    for i in range(len(pos)-1):
        if v[pos[i]] > v[pos[i+1]]: return False
    return True

def bt(st : list, k : int, v : list, current_step : int, step : int) -> tuple[bool, int]:
    for i in range(len(st)):
        st[k] = i
        if ok(st, k):
            if k == len(st) - 1:
                if step != 0 and current_step % step == 0:
                    print("Step ", current_step, ": ")
                    temp = []
                    for j in range(len(st)):
                        temp.append(v[st[j]])
                    print(temp)
                    print()
                if ascending(st, v): 
                    v2 = v.copy()
                    for j in range(len(st)):
                        v2[j] = v[st[j]]
                    v.clear()
                    v.extend(v2)
                    return True, current_step
                return False, current_step
            else:
                if k == len(st) - 2:
                    found, current_step = bt(st, k+1, v, current_step+1, step)
                else:
                    found, current_step = bt(st, k+1, v, current_step, step)
                if found == True:
                    return True, current_step
    return False, current_step

def permutation_sort(v : list, step : int):
    pos = [0] * len(v)
    print("Initial list: ", v)
    print()
    bt(pos, 0, v, 0, step)
    print("Sorted list: ", v)

def compare(v : list, sub_list : list):
    if len(v) == 0:
        return
    sub_list.append(v[0])
    v.pop(0)
    i = 0
    idx = 0
    while i < len(v):
        if v[i] > sub_list[idx]:
            sub_list.append(v[i])
            v.pop(i)
            idx += 1
        else:
            i += 1

def merge(a : list, b : list) -> list:
    ans = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1
    while i < len(a):
        ans.append(a[i])
        i += 1
    while j < len(b):
        ans.append(b[j])
        j += 1
    return ans

def strand_sort(v : list, step : int):
    print("Initial list: ", v)
    print()
    solution = []
    current_step = 0
    while len(v) != 0:
        sub_list = []
        compare(v, sub_list)
        solution = merge(solution, sub_list)
        current_step += 1
        if step != 0 and current_step % step == 0:
            print("Step ", current_step, ": ")
            print("original list: ", v)
            print("sublist: ", sub_list)
            print("solution list: ", solution)
            print()
    v.clear()
    v.extend(solution)
    print("Sorted list: ", v)

def check_sorted(v : list) -> bool:
    for i in range(len(v)-1):
        if v[i] > v[i+1]:
            return False
    return True

def testing(v : list):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Options:")
    print("1 - Clear list")
    print("2 - Modify list")
    if len(v) != 0:
        print("Current list: ", v)
    print("----------------------")
    opt = int(input("Option = "))
    if opt == 1:
        v.clear()
    elif opt == 2:
        line = input("New list = ")
        numbers = line.split(" ")
        temp = []
        for number in numbers:
            temp.append(int(number))
        v.clear()
        v.extend(temp)

def interface():
    done = False
    v_sorted = False
    v = []
    while not done:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Options:")
        print("1 - Generate list")
        print("2 - Exponential search")
        print("3 - Permutation sort")
        print("4 - Strand sort")
        print("5 - Exit")
        if len(v) != 0:
            print("Current list: ", v)
        print("----------------------")
        opt = input("Option = ")
        try: 
            opt = int(opt)
            if opt == 1:
                length = input("length = ")
                try:
                    length = int(length)
                    if length < 0:
                        print("Please enter a natural number")
                        input("Press enter to continue...")
                    else:
                        length = int(length)
                        v = generate_list(length)
                        v_sorted = check_sorted(v)
                except ValueError:
                    print("Please enter a natural number")
                    input("Press enter to continue...")
            elif opt == 2:
                if len(v) == 0: 
                    print("Please generate and sort the list before using the search option")
                    input("Press enter to continue...")
                elif v_sorted == False:
                    print("Please sort the list before using the search option")
                    input("Press enter to continue...")
                else:
                    x = input("What number do you wish to search = ")
                    try:
                        x = int(x)
                        a, b = exponential_search(v, x)
                        if b == -1 or v[b] != x:
                            print("The number ", x, " is not in the list")
                        else:
                            if a == b:
                                print("The number ", x, " is in the list at index", a)
                            else:
                                print("The number ", x, " is in the list at indexes", a, "through", b)
                        input("Press enter to continue...")
                    except ValueError:
                        print("Please enter a natural number")
                        input("Press enter to continue...")
            elif opt == 3:
                if len(v) == 0: 
                    print("Please generate the list first")
                    input("Press enter to continue...")
                elif v_sorted == True:
                    print("The list is already sorted")
                    input("Press enter to continue...")
                else:
                    step = input("step (type 0 to only display initial and final list) = ")
                    try:
                        step = int(step)
                        permutation_sort(v, step)
                        v_sorted = True
                        input("Press enter to continue...")
                    except ValueError:
                        print("Please enter a natural number")
                        input("Press enter to continue...")
            elif opt == 4:
                if len(v) == 0:
                    print("Please generate the list first")
                    input("Press enter to continue...")
                elif v_sorted == True:
                    print("The list is already sorted")
                    input("Press enter to continue...")
                else:
                    step = input("step (type 0 to only display initial and final list) = ")
                    try:
                        step = int(step)
                        strand_sort(v, step) 
                        v_sorted = True
                        input("Press enter to continue...")
                    except ValueError:
                        print("Please enter a natural number")
                        input("Press enter to continue...")
            elif opt == 5:
                done = True
            elif opt == 333:
                testing(v)
                v_sorted = check_sorted(v)
            else:
                print("Please enter a natural number between 1 and 5")
                input("Press enter to continue...")
        except ValueError:
            print("Please enter a number between 1 and 5")
            input("Press enter to continue...")

interface()
