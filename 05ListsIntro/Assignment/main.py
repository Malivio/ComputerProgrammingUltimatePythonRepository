import random

def make_abc():
    return ["a", "b", "c"]

def equal_edges(arr):
    if arr[0] == arr[-1]:
        return True
    else:
        return False

def common_edge(arr1, arr2):
    if arr1[0] == arr2[0] or arr1[0] == arr2[-1]:
        return True
    elif arr1[-1] == arr2[0] or arr1[-1] == arr2[-1]:
        return True
    else:
        return False

def all_the_same(arr):
    if arr[0] == arr[1] and arr[1] == arr[2]:
        return True
    else:
        return False

def all_unique(arr):
    if arr[0] != arr[1] and arr[1] != arr[2] and arr[0] != arr[2]:
        return True
    else:
        return False

def increasing(arr):
    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
        return True
    else:
        return False

def all_true(arr):
    if arr[0] and arr[1] and arr[2]:
        return True
    else:
        return False

def mostly_true(arr):
    if arr.count(True) >= 2:
        return True
    else:
        return False

def random_list(length, amount):
    x = []
    for n in range(amount):
        x.append(random.randint(length[0], length[1]))
    return x

def make_copy(arr):
    #return arr
    return [arr[0], arr[1], arr[2]]

def repeat_thrice(n):
    return[n,n,n]

def make_reversed_copy(arr):
    x = []
    for n in range(len(arr)):
        x.append(arr[-(n+1)])
    return x

def reverse_in_place(arr):
    arr.append(arr[0])
    arr[0] = arr[2]
    arr.pop(2)
    return arr

def main(n = 0):

    if n == 1 or n == 0:
        print("make_abc")
        print(make_abc())
        
        print("equal_edges")
        for iterate in range(5):
            n = random.randint(1,5)
            if n <= 2:
                x = random_list([1,9], 3)
                i = random.randint(1,9)
                x.insert(0, i)
                x.append(i)
                print(x, "=>", equal_edges(x))
            else:
                x = random_list([1,9], 5)
                print(x, "=>", equal_edges(x))

        print("common_edges")
        for iterate in range(5):
            n = [random_list([1,9], 5),random_list([1,9], 5)]
            print(n[0], n[1], "=>", common_edge(n[0], n[1]))

        print("all_the_same")
        for iterate in range(5):
            n = random.randint(1,5)
            if n <= 2:
                x = random.randint(1,9)
                print([x,x,x], "=>", all_the_same([x,x,x]))
            else:
                x = random_list([1,9], 3)
                print(x, "=>", all_the_same(x))
        
        print("all_unique")
        for iterate in range(5):
            n = random.randint(1,7)
            if n == 1:
                x = random.randint(1,9)
                print([x,x,x], "=>", all_unique([x,x,x]))
            else:
                x = random_list([1,9], 3)
                print(x, "=>", all_unique(x))
        
        print("increasing")
        for iterate in range(5):
            n = random.randint(1,5)
            if n <= 2:
                x = random.randint(1,9)
                print([x,x + 1,x + 2], "=>", increasing([x,x + 1,x + 2]))
            else:
                x = random_list([1,9], 3)
                print(x, "=>", increasing(x))
                
        print("all_true")
        for iterate in range(5):
            n = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]
            i = []
            for x in n:
                if x == 1:
                    i.append(True)
                else:
                    i.append(False)
            print(i, "=>", all_true(n))

        print("mostly_true")
        for iterate in range(5):
            n = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]
            i = []
            for x in n:
                if x == 1:
                    i.append(True)
                else:
                    i.append(False)
            print(i, "=>", mostly_true(n))

    if n == 2 or n == 0:
        print("make_copy")
        for iterate in range(5):
            x = [random.randint(1,9), random.randint(1,9), random.randint(1,9)]
            print(x, "=>", make_copy(x))

        print("repeat_thrice")
        for iterate in range(5):
            x = random.randint(1,9)
            print(x, "=>", repeat_thrice(x))

        print("make_reversed_copy")
        for iterate in range(5):
            x = [random.randint(1,9), random.randint(1,9), random.randint(1,9)]
            print(x, "=>", make_reversed_copy(x))

        print("reverse_in_place")
        for iterate in range(5):
            x = [random.randint(1,9), random.randint(1,9), random.randint(1,9)]
            n = x.copy()
            print(n, "=>", reverse_in_place(x))

main()