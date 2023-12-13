import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/4000-most-common-english-words.csv", 'r')
words = f.read().split('\n')
f.close()

def most_vowels():
    word = words[0]
    vowels = 0
    for x in words:
        n = x.count("a") + x.count("e") + x.count("i") + x.count("o") + x.count("u")
        if n > vowels:
            word = x
            vowels = n
    return word

def avg_word_len():
    n = 0
    for x in words:
        n += len(x)
    return round(n/len(words))

def most_common_starting_letter():
    count = {}
    for x in words:
        if x[0] in count.keys():
            count[x[0]] += 1
        else:
            count[x[0]] = 1
    values = list(count.values())
    n = 0
    for x in range(len(values)):
        if values[x] > values[n]:
            n = x
    return list(count.keys())[n]

f = open("../data/gradebook_data.csv", "r")
data = f.read().split('\n')
f.close()
gradebook = []
for g in data:
    gradebook.append(g.split(","))

def all_grades():
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for x in gradebook:
        grade = int(x[2])
        if grade >= 90:
            grades["A"] += 1
        elif grade >= 80:
            grades["B"] += 1
        elif grade >= 70:
            grades["C"] += 1
        elif grade >= 60:
            grades["D"] += 1
        else:
            grades["F"] += 1
    return grades

def avg_grade_levels():
    grades = {"9": 0, "10": 0, "11": 0, "12": 0}
    count = {"9": 0, "10": 0, "11": 0, "12": 0}
    for x in gradebook:
        gradeLevel = x[1]
        grade = int(x[2])
        count[gradeLevel] += 1
        grades[gradeLevel] += grade
    nonZ = {"9": True, "10": True, "11": True, "12": True}
    print(count)
    values = list(count.values())
    for x in range(len(values)):
        if values[x] == 0:
            nonZ[str(x + 9)] = 0 
        else:
            nonZ[str(x + 9)] = grades[str(x + 9)] / count[str(x + 9)]
    return nonZ

def failing_seniors():
    seniors = []
    for x in gradebook:
        if int(x[1]) == 12 and int(x[2]) < 60:
            seniors.append(x[0])
    return seniors

print(most_vowels())

print(avg_word_len())

print(most_common_starting_letter())

print(all_grades())

print(avg_grade_levels())

print(failing_seniors())