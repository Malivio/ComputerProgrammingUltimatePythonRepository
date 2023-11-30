def count_vowels(letters):
    count = 0
    for letter in letters:
        # if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        if letter in ["a", "e", "i", "o", "u"]:
            count = count + 1
    
    return count

inputlist = ["a", "b", "c", "d", "e"]
returnValue = count_vowels(inputlist)
print(returnValue)

def number_product(numbers):
    total = 1
    for number in numbers:
        total = total * number
    
    return total

inputlist = [3, 2, 5]
returnValue = number_product(inputlist)
print(returnValue)

def number_mean(numbers):
    total = 0
    # count = 0
    for number in numbers: 
        total = total + number
        # count = count + 1
    
    # total is the sum of the numbers
    return total / len(numbers)

inputlist = [2, 5, 9, 11]
result = number_mean(inputlist)
print(result)