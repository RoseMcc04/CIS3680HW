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

        # Calculation for full growth period
        full_grow_period = growth_hours // hours_before

        # Calculation for remaining hours due to certain fractional cases
        remaining_hours = growth_hours % hours_before 

        # Population calculation with conditional due to fractional cases
        total_pop = pop_init * (growth_rate ** full_grow_period)
        if remaining_hours > 0:
            partial_rate = 1 + ((growth_rate - 1) * remaining_hours / hours_before)
            total_pop *= partial_rate

        # Output for user
        print(f"The total population is {round(total_pop)}") 


scientist = Biologist()
scientist.popScript()