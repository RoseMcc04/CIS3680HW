"""

Module: biology_app.py
Author: Rose McCormack
Version: 26 September 2024
Description: A biologist needs to predict population growth based on
factors including an initial population, growth rate, the number of
hours to achieve the growth rate, and the number of hours it takes for
the population to grow. 

"""

class Biologist:

    def popScript(self):

        # User input for the initial population
        pop_init = int(input("Enter the initial population: "))

        # User input for growth rate
        growth_rate = float(input("Enter the growth rate (a real number > 1): "))

        # User input for number of hours to achieve growth
        hours_before = int(input("Enter the number of hours to achieve the growth rate: "))

        # User input for total hours of growth
        growth_hours = int(input("Enter the total hours of growth: "))

        # Total population loop structure
        pop_total = pop_init
        i = 0
        while i < growth_hours:
            i += hours_before
            pop_total *= growth_rate
        
        # Print statement for final output
        print(f"The total population is {int(pop_total)} organisms.")


scientist = Biologist()
scientist.popScript()