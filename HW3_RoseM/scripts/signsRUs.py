"""

Module: signsRUs.py
Author: Rose McCormack
Version: 26 September 2024
Description: A business called Signs-R-Us makes personalized signs. They
would like an application to compute the price of a sign based on certain
factors. 

"""

class Script:

    def signsRUs(self):

        # Total cost variable that will get added onto
        total_cost = 0

        # First prompt to ask about sign material
        sign_material = input("Enter sign material (Oak or Pine): ")

        # Second prompt for text the user wants on the sign
        sign_text = input("Enter sign text: ")

        # Third prompt for the letter color the user wants on the sign
        sign_color = input("Enter letter color (Black, White, or Gold): ")

        # First conditional to add onto total cost
        if sign_material == "Oak":
            total_cost += 15.00
        
        # Loop structure to look at string chars
        i = 0
        for i in range(len(sign_text)):
            if (i > 5):
                total_cost += 3.00
        
        # Second conditional to add onto total cost
        if sign_color == "Gold":
            total_cost += 12.00
        
        # Minimum charge is $30.00
        total_cost += 30.00
        
        # Print statement for user output
        print(f"The total cost of the sign is ${round(total_cost, 2)}.")

prompt = Script()
prompt.signsRUs()