# # simple application
# response = ""

# while response != "y":
#     print("type y:")
#     response = input()

def is_digit(character):
    if character in "0123456789":
        return True
    else: 
        return False

def is_letter(character):
    if character in "abcdefghijklmnopqrstuvwxyz":
        return True
    else:
        return False
    


def get_valid_username():
    proposed_username = ""
    invalid_username = True
    while invalid_username == True:
        print("please enter a username")
        proposed_username = input()

        if is_digit(proposed_username[0]) and is_digit(proposed_username[1]) and is_letter(proposed_username[2]) and is_letter(proposed_username[3]) and is_letter(proposed_username[4]) and is_letter(proposed_username[5]) and is_letter(proposed_username[6]):
            invalid_username = False

    
    print("Welcome to the system", proposed_username)


get_valid_username()