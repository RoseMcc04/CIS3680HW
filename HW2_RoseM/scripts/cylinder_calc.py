from math import pi

"""
Module: cylinder_calc.py
Author: Rose McCormack
Version: 13 September 2024
Description: This Python script will allow the user to enter a radius 
and height. Then, the user will determine if the user wants the value 
rounded or not. Finally, the user will retrieve their desired output. 
"""

class Calc:

    def cylinder_calc(self):

        """
        Calls itself and allows the user to input a radius and height
        that will eventually output the volume and surface area of a 
        cylinder. 

        Parameters:
        self: Reference keyword

        Returns:
        int, float: Returns a value depending on the user's preference.

        Example:
        >>> calcObject.cylinder_calc()
        # Prompts follow
        """

        # Radius of the cylinder
        radius = float(input("Please enter the radius of the cylinder in decimal form (Ex. 4.55): "))

        # Height of the cylinder
        height = float(input("Pleae enter the height of the cylinder in decimal form (Ex. 4.55): "))

        # Volume formula for cylinder
        volume = pi * (radius ** 2) * height

        # Surface area formula for cylinder
        surface_area = (2 * pi * radius * height) + (2 * pi * (radius ** 2))

        # Decision input for rounding
        decision = input("Do you want to round your answer? ")
        
        # Conditional block if decision is yes or no to round
        if decision == "yes":
            roundPlace = int(input("How many decimal places do you want to round to? "))
            
            # Nested conditional if the user wants to round to a specific place or not
            if roundPlace == 0:
                print(f"The volume of the cylinder is {round(volume)} cubic units.")
                print(f"The surface area of the cylinder is {round(surface_area)} square units.")
            else:
                print(f"The volume is {round(volume, roundPlace)} cubic units.")
                print(f"The surface area is {round(surface_area, roundPlace)} square units.")
        else:
            print(f"The volume of the cylinder is {round(volume, 2)} cubic units.")
            print(f"The surface area of the cylinder is {round(surface_area, 2)} square units.")


# Calculator object that will call the desired function/script
calc_object = Calc()
calc_object.cylinder_calc()
