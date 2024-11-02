"""

Module: guess_game.py
Author: Rose McCormack
Version: 20 October 2024
Description: Create a program for the guessing game where the 
computer provides the guesses and can tell if you are cheating.

"""

class Script:
    def script(self):
        # User input for lower bound
        lower = float(input("Enter the smaller number: "))
        # User input for upper bound
        upper = float(input("Enter the larger number: "))
        
        # Counter variable for user attempts
        tries = 0
        while lower <= upper:
            # Generated guess along with an increase of one try for 
            # each iteration. 
            guess = (lower + upper) // 2
            tries += 1
            
            # Print statements for the upper and lower bound, along with
            # the guess. 
            print(f"{lower} {upper}")
            print(f"Your number is {guess}")

            # User feedback input along with .strip() for removing
            # unneccesary whitespace. 
            feedback = input("Enter =, <, or >: ").strip()

            # Conditional block to determine the guess from feedback
            # input. 
            if feedback == "=":
                print(f"Hooray, I've got it in {tries} tries!")
                return
            elif feedback == "<":
                upper = guess - 1
            elif feedback == ">":
                lower = guess + 1
            else:
                print("Invalid input. Please enter =, <, or >.")
                continue

            # Conditional to see if the user is cheating.
            if lower > upper:
                print("I'm out of guesses and you cheated!")
                continue

execution = Script()
execution.script()
