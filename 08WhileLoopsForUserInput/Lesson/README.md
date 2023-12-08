This topic is largely about handling user input. So we won't be testing our functions in an automated way, passing in arguments and returning values. Instead, we'll type in text at the prompts, like a human.

We will wrap every exercise inside a function that takes no arguments and doesn't return anything (just to organize our code, and to allow us to test it bit-by-bit).

1. `get_valid_username`

   Suppose a student is signing up for an online account. They are asked to type in their username, which must be their two digit graduation year, followed by the first five letters of their full name. For example, "25alexw"

   Write code that will repeatedly ask the user for their username until it is in the correct format (two digits followed by 5 letters), then print them a welcome message.

   Write helper functions `is_digit` and `is_letter` to make the code more readable and extensible. Python already has many of these utilities, but writing them ourselves is instructive.
