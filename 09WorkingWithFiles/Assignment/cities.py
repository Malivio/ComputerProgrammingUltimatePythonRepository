import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open('../data/1000-largest-us-cities.json', 'r')
cities = json.load(f)
f.close()

def kansas_cities():
    cities1 = []
    for x in cities:
        if x['state'] == 'Kansas':
            cities1.append(x['city'])
    return cities1

def longest_name():
    l = 0
    city = ''
    for x in cities:
        if len(x['city'].replace(' ','')) > l:
            l = len(x['city'].replace(' ',''))
            city = x['city']
    return l, city

def farthest_cardinal():
    d = {'north': 0, 'south': 0, 'east': 0, 'west': 0}
    for x in cities:
        lat = x['latitude']
        lon = x['longitude']
        if lat > d['north']:
            d['north'] = lat
        elif lat > -(d['south']):
            d['south'] = lat
        if lon > d['east']:
            d['east'] = lon
        elif lon < -(d['west']):
            d['west'] = lon
    return d

def growing_shrinking():
    growth = {'city': '', 'pop': 0}
    shrink = {'city': '', 'pop': 0}
    for x in cities:
        pop = x['growth_from_2000_to_2013'].replace('%','')
        if not pop == "":
            if float(pop) > growth['pop']:
                growth['pop'] = float(pop) 
                growth['city'] = x['city']
            elif float(pop) < shrink['pop']:      
                shrink['pop'] = float(pop)
                shrink['city'] = x['city']
    return [growth, shrink]

def state_highest_pop():
    pop = {}
    for x in cities:
        if x['cities'] in pop.keys():
            pop[x['cities']] += int(x['population'])
    n = 0
    values = list(pop.values())
    for x in range(len(values)):
        if values[x] > n:
            n = values[x]
    return None

def fastest_pop():
    growth = {"city": '', "pop": 0}
    shrink = {"city": '', 'pop': 0}
    for x in range(len(cities)):
        city = cities[x]
        g = city['growth_from_2000_to_2013'].replace('%', '')
        if not g == "":
            pop = int(city['population']) * float(g) / 100
            if pop > growth['pop']:
                growth['city'] = city['city']
                growth['pop'] = pop
            elif pop < shrink['pop']:
                shrink['city'] = city['city']
                shrink['pop'] = pop
    return growth, shrink

print(kansas_cities())

print(longest_name())

print(farthest_cardinal())

print(growing_shrinking())

print(state_highest_pop())

print(fastest_pop())