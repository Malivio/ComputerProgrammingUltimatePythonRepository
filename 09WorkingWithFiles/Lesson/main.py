import csv
import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()


def find_longest_word(wordlist):
    longest_so_far = ""
    for word in wordlist:
        if len(word) > len(longest_so_far):
            longest_so_far = word
    return longest_so_far

print(find_longest_word(words))



f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 
longest_name = ""
for row in reader:
    name, gradelevel, percent = row
    gradelevel = int(gradelevel)
    print(gradelevel)
    if gradelevel==12 and len(name) > len(longest_name):
        longest_name = name

print("senior with longest name is: ", longest_name)
f.close()

f = open("../data/1000-largest-us-cities.json", "r")
cities = json.load(f)
f.close()

print(cities[0]["city"])
print(cities[1]["latitude"])

total_population = 0
for city in cities:
    if city["state"] == "Kansas":
        total_population = total_population + int(city["population"])

print("population in kansas cities is:", total_population)

