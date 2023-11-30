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
    
    print("count_act_scores")
    for iterate in range(5):
        n = []
        for j in range(5):
            n.append(random.randint(-10, 100))
        print(n, "=>", number_sum(n))

    print("count_act_scores")
    for iterate in range(5):
        n = []
        for j in range(5):
            n.append(random.randint(-20, 50))
        print(n, "=>", average_act_score(n)) 
main()