"""

Module: highCServices.py
Author: Rose McCormack
Version: 20 September 2024
Description: This is a script written for a High Country company that 
services homeowners and businesses with powerwashing, especially for
mold and mildew. The script will ask the user to input the height and
width of a home's outside dimensions to determine the surface area
to spray the walls and roof. We will also round the liters of solution 
using the round() function from the math module. 

"""

class highCServices:

    def cleanFunc(self):

        # Constant for price of a liter for solution
        LITER_PRICE = 48.00

        # Length dimension of a wall of the house
        wall_length = float(input("Enter the length of the side of the wall in feet in decimal form (ex. 3.45): \n"))

        # Height dimension for a wall of the house
        wall_height = float(input("Enter the height of the side of the wall in feet in decimal form (ex. 3.45): \n"))

        # The amount of walls needed to be sprayed
        wall_count = int(input("Enter the number of walls to be sprayed: \n"))

        # Length of the slope of the roof
        roof_slope_len = float(input("Enter the length of the roof slope in feet in decimal form (ex. 3.45): \n"))

        # Length of the side of the roof
        roof_side_len = float(input("Enter the length of the side of the roof in feet in decimal form (ex. 3.45): \n"))

        # Constant for determining square feet/liter
        RATE = 300 / LITER_PRICE

        # Surface area formula for the house
        surface_area = wall_count * (wall_length * wall_height) + 2 * (roof_slope_len * roof_side_len)

        # Total cost formula
        total_cost = surface_area * RATE

        # print statements for the results
        print(f"The total surface area of your house is {round(surface_area, 2)} sq. feet.\n")
        print(f"The total cost of the cleaning will be ${round(total_cost, 2)}.\n")

# highCServices object called client
client = highCServices()
# client calls the script used to determine the total price
client.cleanFunc()