import random

def make_abc():
    return ["a", "b", "c"]

def equal_edges(arr):
    if arr[0] == arr[-1]:
        return True
    else:
        return False

def common_edge(arr1, arr2):
    if arr1[0] == arr2[0] or arr1[0] == arr2[1]:
        return True
    elif arr1[1] == arr2[0] or arr1[1] == arr2[1]:
        return True
    else:
        return False

def all_the_same(arr):
    if arr[0] == arr[1] and arr[1] == arr[2]:
        return True
    else:
        return False

def all_unique(arr):
    if arr[0] == arr[1] or arr[1] == arr[2] or arr[0] == arr[2]:
        return False
    else:
        return True

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
        x.push(random.randint(length[0], length[1]))
    return x

def main():
    print("make_abc")
    print(make_abc())
    print("\n")

    print("equal_edges")
    for iterate in range(5):
        n = random.randint(1,5)
        if n <= 2:
            x = random_list([1,9], 3)
            i = random.randint(1,9)
            x.insert(0, i)
            x.insert(-1, i)
            print(x, equal_edges(x))


main()