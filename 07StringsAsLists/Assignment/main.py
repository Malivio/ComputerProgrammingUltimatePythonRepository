def is_alliteration(str1, str2): return str1[0] == str2[0]

def count_vowels(str1): return str1.count("a") + str1.count("e") +  str1.count("i") +  str1.count("o") +  str1.count("u")

def count_numbers(str1): 
    n = 0
    for x in str1:
        try:
            int(x)
        except:
            continue
        n += 1
    return n

def count_target_letters(str1, char): return str1.count(char)

def in_alphabetical_order(str1):
    for x in range(len(str1) - 1):
        if not ord(str1[x].lower()) == ord(str1[x + 1].lower()) - 1:
                return False
    return True

def alternating_case(word):
    i = ""
    for x in range(len(word)):
        if int(x/2) == x/2:
            i += word[x].upper()
        else:
            i += word[x]
    return i

def remove_vowels(str1): return str1.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")

def to_camel_case(str1):
    str1.strip()
    str2 = str1[0]
    for x in range(len(str1) - 1):
        if str1[x] == " ":
            str2 += str1[x + 1].upper()
        else:
            str2 += str1[x + 1]
    return str2.replace(" ", "")

def to_snake_case(str1): return str1.replace(" ", "_")

def without_duplicates(arr1):
    i = [arr1[0]] 
    for x in arr1:
            if i[-1] != x:
                i.append(x)
    return i

def filter_valid_act_scores(arr1):
    i = []
    for x in arr1: 
        if x <= 36 and x >= 1:
            i.append(x)
    return i