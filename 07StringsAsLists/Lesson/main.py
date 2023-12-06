def is_plural(word):
    if word[-1] == "s":
        return True
    else:
        return False

print(is_plural("apple"))
print(is_plural("apples"))
print(is_plural("has"))

def has_vowel(word):
    for letter in word:
        if letter in "aeiou":
            return True
    return False

print(has_vowel("sky"))
print(has_vowel("apple"))
print(has_vowel("bcdfghj"))

def last_in_alphabet(word):
    winner = "a"
    for letter in word:
        if letter > winner:
            winner = letter
    return winner

print(last_in_alphabet("sky"))
print(last_in_alphabet("apple"))
print(last_in_alphabet("bcdfghj"))


# to add elements to the end of a list:
mylist = [1, 2, 3]
mylist.append(4)
print(mylist)

# to add elements to the end of a string:
mystring = "abc"
mystring = mystring + "d"

"a very useful pot".title()
def to_title_case(string):
    result = ""
    next_upper = True
    for letter in string:
        if letter == " ":
            next_upper = True
            result = result + letter
        elif next_upper == True:
            result = result + letter.upper()
            next_upper = False
        else:
            result = result + letter
    
    return result

print(to_title_case("a very useful pot"))

def without_zeros(numbers):
    result = []
    for number in numbers:
        if number == 0:
            pass
        else:
            result.append(number)
    return result

print(without_zeros([31, 0, 32, 0, 0, 5]))




