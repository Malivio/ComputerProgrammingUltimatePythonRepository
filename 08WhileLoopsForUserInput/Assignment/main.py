import random

def number_guesser():
    print("number_guesser")
    n = random.randint(1, 10)
    print("Enter A Number")
    while True:
        x = input()
        if not x.isdigit():
            print("Invalid Input")
            continue
        x = int(x)
        if n == x:
            print("Correct")
            break
        else:
            if n > x:
                print("Higher")
            else:
                print("Lower") 

#number_guesser()

def number_guesser_with_lives():
    print("number-guesser_with_lives")
    lives = 3
    n = random.randint(1, 10)
    print("Enter A Number")
    while True:
        x = input()
        if not x.isdigit():
            print("Invalid Input")
            continue
        x = int(x)
        if n == x:
            print("Correct")
            break
        elif lives == 1:
            print("Game Over: Answer was", n)
        else:
            if n > x:
                lives -= 1
                print("Higher")
            else:
                lives -= 1
                print("Lower") 
            print("Lives:", lives)

#number_guesser_with_lives()

def vending_machine():
    payment = 0
    print("vending_machine")
    print("Pay Up")
    while True:
        x = input()
        if x.isdigit():
            if not int(x) in [5,10,25]:
                print("Only Quarters, Dimes, and Nickles")
            else:
                payment += int(x)
                if payment > 50:
                    print("Change Due", payment - 50)
                    break
        else:
            print("Please Use Coins")

#vending_machine()

words = ["Hello", "Goodbye", "Good", "Happy", "Sad", "Bad", 'Hurt', 'Mad', 'Angry', 'Fine']

levels = {5: "|\n|  |\n|", 4: "|\n|-|\n|", 3: "|\n|-|-\n|", 2: "|\n|-|-\n|/", 1: "|\n|-|-\n|/ \\", 0: "| _ \n||_|\n|-|-\n|/ \\"}

def hangman():
    print("hangman")
    word = words[random.randint(0, len(words) - 1)]
    lives = 6
    guess = []
    for iterate in range(len(word)):
        guess.append('_')
    print("Guess The Word")
    while True:
        x = input()
        if len(x) != 1:
            print("Enter Only 1 Letter")
            continue
        elif x in word:
            if not x in guess:
                for n in range(len(word)):
                    if word[n] == x:
                        guess[n] = x
            else:
                print("YOU ALREADY GUESSED THIS")
        else:
            print("None")
            lives -= 1
            if lives == 0:
                print("Game Over")
                print("_____")
                print(levels[lives])
                print("|____")
                break
            else:
                print('Lives:', lives)
            print("_____")
            print(levels[lives])
            print("|____")
        prn = ""
        for i in guess:
            prn += i
        print(prn)

hangman()



