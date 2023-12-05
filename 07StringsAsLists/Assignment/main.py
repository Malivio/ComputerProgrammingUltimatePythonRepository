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