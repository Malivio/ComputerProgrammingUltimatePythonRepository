import random

def count_failing_grades(grades):
    n = 0
    for x in grades:
        if x < 60:
            n += 1
    return n

def count_act_scores(scores):
    n = 0
    for x in scores:
        if x <= 36 or x >= 1:
            n += 1
    return n

def number_sum(arr):
    n = 0
    for x in arr:
        n += x
    return n

def average_act_score(scores):
    n = 0
    i = 0
    for x in scores:
        if x <= 36 or x >= 1:
            n += x
            i += 1
    return n/i

def all_true(arr): return not False in arr and len(arr) > 0

def any_true(arr): return True in arr and len(arr) > 0

def mostly_true(arr): return arr.count(True) > arr.count(False)

def has_vowel(arr):
    for l in arr:
        if l.lower() in ["a", 'i', 'e', 'o', 'u']:
            return True
    return False

def all_the_same(arr): return arr.count(arr[0]) == len(arr)

def increasing(arr):
    for x in range(len(arr) - 1):
        if arr[x] >= arr[x + 1]:
            return False
    return True

def is_incrementing(arr):
    for x in range(len(arr) - 1):
        if arr[x] != arr[x + 1]:
            return False
    return True

def has_adjacent_repeat(arr):
    for x in range(len(arr) - 1):
        if arr[x] == arr[x + 1]:
            return True
    return False

def sum_with_skips(arr):
    n = 0
    skip = False
    for x in arr:
        if x == -1:
            if skip:
                skip = False
            else:
                skip = True
        elif not skip:
            n += x
    return n

def randomList():
    n = []
    for x in range(random.randint(0,9)):
        n.append(bool(random.randint(0,1)))
    return n

def main():
    print("count_failing_grades")
    for iterate in range(5):
        n = []
        for j in range(10):
            n.append(random.randint(0, 100))
        print(n, "=>",count_failing_grades(n))

    print("count_act_scores")
    for iterate in range(5):
        n = []
        for j in range(10):
            n.append(random.randint(-20, 50))
        print(n, "=>",count_act_scores(n))
    
    print("number_sum")
    for iterate in range(5):
        n = []
        for j in range(5):
            n.append(random.randint(-10, 100))
        print(n, "=>", number_sum(n))

    print("average_act_score")
    for iterate in range(5):
        n = []
        for j in range(5):
            n.append(random.randint(-20, 50))
        print(n, "=>", average_act_score(n)) 

    print("all_true")
    for iterate in range(5):
        n = randomList()
        print(n, "=>", all_true(n))
        
    print("any_true")
    for iterate in range(5):
        n = randomList()
        print(n, "=>", any_true(n))

    print("mostly_true")
    for iterate in range(5):
        n = randomList()
        print(n, "=>", mostly_true(n))

    numToLetter = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
    print("has_vowel")
    for iterate in range(5):
        letters = []
        for x in range(5):
            letters.append(numToLetter[random.randint(0,25)])
        print(letters, '=>', has_vowel(letters))
        
    print("all_the_same")
    for iterate in range(5):
        n = random.randint(1,9)
        arr = [n]
        for iter in range(2):
            if random.randint(0,1):
                arr.append(n)
            else:
                arr.append(random.randint(1,9))
        print(arr, "=>", all_the_same(arr))

    print("increasing")
    for iterate in range(5):
        n = random.randint(1,9)
        arr = [n]
        for iter in range(random.randint(2,4)):
            if random.randint(0,1):
                n += random.randint(1,3)
                arr.append(n)
            else:
                arr.append(random.randint(1,9))
        print(arr, "=>", increasing(arr))

    print("is_incrementing")
    for iterate in range(5):
        n = random.randint(1,9)
        arr = [n]
        for iter in range(random.randint(2,4)):
            if random.randint(0,1):
                arr.append(n + 1)
            else:
                arr.append(random.randint(1,9))
        print(arr, "=>", is_incrementing(arr))
    
    print("has_adjacent_repeat")
    for iterate in range(5):
        arr = []
        for iter in range(5):
            arr.append(random.randint(1,9))
        print(arr, "=>", has_adjacent_repeat(arr))

    print("sum_with_skips")
    for iterate in range(5):
        arr = []
        for iter in range(random.randint(5,9)):
            arr.append(random.randint(1,9))
        x = random.randint(0,len(arr) - 1)
        y = random.randint(0,len(arr) - 1)
        if x == y:
            for lll in arr:
                lll = random.randint(1,9)
        else:
            arr[x] = -1
            arr[y] = -1
        print(arr, "=>", sum_with_skips(arr))


main()