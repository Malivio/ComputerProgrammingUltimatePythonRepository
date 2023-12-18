import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open('../data/childDetails.json', 'r')
data = json.load(f)
f.close()

def longest_name():
    names = []
    l = 0
    for x in data:
        names.append(x['name'])
        for i in x['guardians']:
            names.append(i['name'])
        for i in x['guardians']:
            names.append(i['name'])
    n = 0
    y = 0
    for x in names:
        if len(x) > l:
            l = len(x)
            y = n
        n += 1
    return names[y]

def household_incomes():
    lowest = {'income': 1000000000000, 'name': ''}
    highest = {'income': 0, 'name': ''}
    for x in data:
        overall = 0
        for i in x['guardians']:
            overall += i['salary']
        if overall > highest['income']:
            highest['income'] = overall
            highest['name'] = x['name']
        elif overall < lowest['income']:
            lowest['income'] = overall
            lowest['name'] = x['name']
    return highest, lowest

def highest_inherence():
    lowest = {'income': 100000000000, 'name': ''}
    highest = {'income': 0, 'name': ''}
    for x in data:
        overall = 0
        for i in x['guardians']:
            overall += i['salary']
        if overall / (len(list(x['siblings'])) + 1) > highest['income']:
            highest['income'] = overall
            highest['name'] = x['name']
        elif overall / (len(list(x['siblings'])) + 1) < lowest['income']:
            lowest['income'] = overall
            lowest['name'] = x['name']
    return highest, lowest

print(longest_name())

print(household_incomes())

print(highest_inherence())