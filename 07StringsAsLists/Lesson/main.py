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



