import math

"""

Author: Rose McCormack
Version: 3 September 2024

Description: We are making a function for a user to input their
height and weight in the customary system, and then the user will
retrieve the output as their body mass index (BMI). 

"""

class BMICalc:

    def calculator(self):
        lbs = float(input("What is your weight in pounds?: "))
        inches = float(input("What is your height in inches?: "))
    
        kg = lbs / 2.205
        meters = inches * 0.0254

        bmi = round(kg / (meters ** 2), 2)
        print(f"Your BMI is {bmi}.")

bmi_calculator = BMICalc()
bmi_calculator.calculator()