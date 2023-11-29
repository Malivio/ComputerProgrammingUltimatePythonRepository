def make_pi():
    result = [3, 1, 4]
    return result

print("Demonstrate make pi:")
print(make_pi())

def edges_sum(items):
    first = items[0]
    last = items[-1]
    result = first + last
    return result

print("Demonstrate edges_sum")
print("[1, 2, 3, 11] -> ", edges_sum([1, 2, 3, 11]))

def are_reversed(list1, list2):
    # first1, middle1, last1 = list1
    first1 = list1[0]
    first2 = list2[0]
    middle1 = list1[1]
    middle2 = list2[1]
    last1 = list1[2]
    last2 = list2[2]

    if first1 == last2 and middle1 == middle2 and last1 == first2:
        return True
    else: 
        return False

print("Demonstrate are_reversed")
print("[1, 2, 4] & [3, 2, 1] -> ", are_reversed([1, 2, 4], [3, 2, 1]))

def make_repeated_max(items):
    maxvalue = max(items)
    return [maxvalue, maxvalue, maxvalue]

print("Demonstrate make_repeated_max")
original_list = [3, 5, 1]
new_list = make_repeated_max(original_list)
print("original list: ", original_list)
print("new list: ", new_list)


def overwrite_with_max(items):
    maxvalue = max(items)
    items[0] = maxvalue
    items[1] = maxvalue
    items[2] = maxvalue

    return items

print("Demonstrate overwrite_with_max")
original_list = [3, 5, 1]
new_list = overwrite_with_max(original_list)
print("original list: ", original_list)
print("new list: ", new_list)
