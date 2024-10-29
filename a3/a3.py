import os
import random
import timeit
from texttable import Texttable
from itertools import permutations

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

def permutation_sort(v : list, step : int):
    if step != 0:
        print("Initial list:", v)
    current_step = 0
    for i in permutations(v):
        temp = list(i)
        current_step += 1
        if temp == sorted(temp):
            v.clear()
            v.extend(temp)
            break
        if step != 0 and current_step % step == 0:
            print("Step", current_step, ":")
            print(temp)
            print()
    if step != 0:
        print("Sorted list:", v)

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
    if step != 0:
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
    if step != 0:
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

def best_case():
    # best cases:
    # permutation sort: the list is already sorted, so it only checks it once, O(n) complexity
    # strand sort: the list is already sorted, so the sublist becomes the whole initial list, O(n) complexity
    # exponential search: the element searched for is the first one, so it only searches in the interval [0, 0], O(1)

    t = Texttable()
    t.add_row(["List length", 500, 1000, 2000, 4000, 8000])
    t.set_precision(6)
    list_len = 500 
    row1 = ["Permutation sort"]
    row2 = ["Strand sort"]
    row3 = ["Exponential search"]
    while list_len <= 8000:
        temp = generate_list(list_len)
        temp = sorted(temp)
        exec_time = timeit.timeit(lambda : permutation_sort(temp, 0), number = 1)
        row1.append(exec_time)
        temp = sorted(temp)
        exec_time = timeit.timeit(lambda : strand_sort(temp, 0), number = 1)
        row2.append(exec_time)
        temp = sorted(temp)
        exec_time = timeit.timeit(lambda : exponential_search(temp, temp[0]), number = 1)
        row3.append(exec_time)
        list_len *= 2
    t.add_row(row1)
    t.add_row(row2)
    t.add_row(row3)
    print(t.draw())
    print()

def worst_case():
    # worst cases:
    # permutation sort: the list is sorted in descending order, so we have to generate all permutations to reach
    # the ascending one, O(n!) complexity
    # strand sort: the list is sorted in descending order, so for each of the N elements we merge, O(n^2) complexity
    # exponential search: the element searched for is not in the list, so O(log2 N) complexity

    t = Texttable()
    t.add_row(["List length", 500, 1000, 2000, 4000, 8000])
    t.set_precision(6)
    list_len = 500 
    row2 = ["Strand sort"]
    row3 = ["Exponential search"]
    while list_len <= 8000:
        temp = generate_list(list_len)
        temp = sorted(temp, reverse = True)
        exec_time = timeit.timeit(lambda : strand_sort(temp, 0), number = 1)
        row2.append(exec_time)
        temp = sorted(temp)
        exec_time = timeit.timeit(lambda : exponential_search(temp, 1005), number = 1)
        row3.append(exec_time)
        list_len *= 2
    t.add_row(row2)
    t.add_row(row3)
    print(t.draw())
    t2 = Texttable()
    t2.add_row(["List length", 6, 7, 8, 9, 10])
    t2.set_precision(6)
    list_len = 6 
    row = ["Permutation sort"]
    while list_len <= 10:
        temp = generate_list(list_len)
        temp = sorted(temp, reverse = True)
        exec_time = timeit.timeit(lambda : permutation_sort(temp, 0), number = 1)
        row.append(exec_time)
        list_len += 1
    t2.add_row(row)
    print()
    print(t2.draw())
    print()

def average_case():
    t = Texttable()
    t.add_row(["List length", 500, 1000, 2000, 4000, 8000])
    t.set_precision(6)
    list_len = 500 
    row2 = ["Strand sort"]
    row3 = ["Exponential search"]
    while list_len <= 8000:
        temp = generate_list(list_len)
        exec_time = timeit.timeit(lambda : strand_sort(temp, 0), number = 1)
        row2.append(exec_time)
        random.shuffle(temp)
        pos = random.randrange(0, len(temp)-1)
        exec_time = timeit.timeit(lambda : exponential_search(temp, temp[pos]), number = 1)
        row3.append(exec_time)
        list_len *= 2
    t.add_row(row2)
    t.add_row(row3)
    print(t.draw())
    print()
    t2 = Texttable()
    t2.add_row(["List length", 6, 7, 8, 9, 10])
    t2.set_precision(6)
    list_len = 6 
    row = ["Permutation sort"]
    while list_len <= 10:
        temp = generate_list(list_len)
        exec_time = timeit.timeit(lambda : permutation_sort(temp, 0), number = 1)
        row.append(exec_time)
        list_len += 1
    t2.add_row(row)
    print()
    print(t2.draw())
    print()

def interface():
    done = False
    v_sorted = False
    v = []

    def generate_list_opt():
        nonlocal v, v_sorted
        length = input("length = ")
        try:
            length = int(length)
            if length < 0:
                print("Please enter a natural number")
            else:
                length = int(length)
                v = generate_list(length)
                v_sorted = check_sorted(v)
        except ValueError:
            print("Please enter a natural number")

    def exponential_search_opt():    
        if len(v) == 0: 
            print("Please generate and sort the list before using the search option")
        elif v_sorted == False:
            print("Please sort the list before using the search option")
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
            except ValueError:
                print("Please enter a natural number")

    def permutation_sort_opt():
        nonlocal v_sorted
        if len(v) == 0: 
            print("Please generate the list first")
        elif v_sorted == True:
            print("The list is already sorted")
        else:
            step = input("step (0 for no prints) = ")
            try:
                step = int(step)
                permutation_sort(v, step)
                v_sorted = True
            except ValueError:
                print("Please enter a natural number")

    def strand_sort_opt():
        nonlocal v_sorted
        if len(v) == 0:
            print("Please generate the list first")
        elif v_sorted == True:
            print("The list is already sorted")
        else:
            step = input("step (0 for no prints) = ")
            try:
                step = int(step)
                strand_sort(v, step) 
                v_sorted = True
            except ValueError:
                print("Please enter a natural number")

    def best_case_opt():
        best_case()

    def worst_case_opt():
        worst_case()

    def average_case_opt():
        average_case()

    def exit_opt():
        nonlocal done
        done = True

    def testing_opt():
        nonlocal v_sorted
        testing(v)
        v_sorted = check_sorted(v)

    options = {
        1: generate_list_opt,
        2: exponential_search_opt,
        3: permutation_sort_opt,
        4: strand_sort_opt,
        5: best_case_opt,
        6: worst_case_opt,
        7: average_case_opt,
        8: exit_opt,
        333: testing_opt
    }

    while not done:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Options:")
        print("1 - Generate list")
        print("2 - Exponential search")
        print("3 - Permutation sort")
        print("4 - Strand sort")
        print("5 - Test best case")
        print("6 - Test worst case")
        print("7 - Test average case")
        print("8 - Exit")
        if len(v) != 0:
            print("Current list: ", v)
        print("----------------------")
        opt = input(" >>> ")
        try: 
            opt = int(opt)
            if opt in options:
                options[opt]()
            else:
                print("Please enter a number between 1 and 8")
        except ValueError:
            print("Please enter a number between 1 and 8")
        if opt != 8:
            input("Press enter to continue...")

interface()
