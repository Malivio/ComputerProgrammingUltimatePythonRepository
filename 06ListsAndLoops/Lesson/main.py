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

def all_vowels(letters):
    # # using previous function
    # number_of_vowels = count_vowels(letters)
    # if number_of_vowels == len(letters):
    #     return True
    # else:
    #     return False

    # from scratch (faster to execute)
    for letter in letters:
        if letter not in ["a", "e", "i", "o", "u"]:
            return False
    return True

print(all_vowels(["a", "e", "a", "i", "u", "o"]))
print(all_vowels(["a", "e", "s", "i", "u", "o"]))

def sum13(nums):
    total = 0
    just_saw_13 = False
    for num in nums:
        if num == 13:
            just_saw_13 = True
        elif just_saw_13 == True:
            just_saw_13 = False
        else:
            total = total + num

    return total

def sum67(nums):
    total = 0
    ignoring = False

    for num in nums:
        if num == 6:
            ignoring = True
        elif ignoring == True and num == 7:
            ignoring = False
        elif ignoring == False:
            total = total + num
    
    return total