Just like in the lesson, these exercises will be unusual functions: they will take no arguments and not return anything, and will prompt the user for input within them.

1. `number_guesser`

   Use `random.randint(1, 10)` to generate a secret number from 1 to 10. Then ask the user to guess the secret number. Keep asking them to guess until they guess the correct number. If they guess an incorrect number, tell them whether they were too high or too low. Handle invalid user input (e.g. if the user typed a string instead of a number at the prompt) without crashing.

1. `number_guesser_with_lives`

   Just like the previous exercise, except the user starts with three lives, and loses one for every incorrect guess. They should not lose a life for invalid user input. The game ends when either they have guessed the correct number, or when they have run out of lives.

1. `vending_machine`

   A vending machine charges you 50 cents for a snack. The vending machine only accepts quarters, dimes, and nickels. It should display the amount due and prompt the user to enter a coin. The user should enter a number representing the coin they insert (25, 10, or 5). The amount due should then be updated, and the user prompted to enter another coin. This should continue until the user has entered enough money. At that point, the vending machine should display how much change it will give the user. If an invalid coin is entered, the vending machine should ignore it (and not reduce the amount due). For example:

   ```
   Amount due: 50
   Insert coin: 25
   Amount due: 25
   Insert coin: 10
   Amount due: 15
   Insert coin: 100
   Amount due: 15
   Insert coin: 5
   Amount due: 10
   Insert coin: 1
   Amount due: 10
   Insert coin: 25
   Change given: 15
   ```

1. `hangman` (+)

   Write a hangman game.
