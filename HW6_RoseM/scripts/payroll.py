"""
Author: Rose McCormack
Version: 2 November 2024
Module: payroll.py
Description: 

The Payroll Department keeps a list of employee 
information for each pay period in a text file. The format of 
each line of the file is the following:

<last name> <hourly wage> <hours worked>

Write a program that inputs a filename from the user and prints 
to the terminal a report of the wages paid to the employees for 
the given period. The report should be in tabular format with the 
appropriate header. Each line should contain an employee's name, 
the hours worked and the wages paid for that period.
"""

# Function built from the script
def main():

    # Exception block for file input in case file does not exist anymore
    filename = input("Enter the file name: ")
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print(f"{filename} not found")
        return

    # Printed header with string formatting
    print(f'{"Name":<15}{"Hours":<11}{"Total Pay":<10}')

    # Loop structure that prints output from the file
    for line in f:
        parts = line.split()

        # Making sure lines are formatted properly in the file
        if len(parts) != 3:
            continue

        # Employee details
        name = parts[0]
        hourly_wage = float(parts[1])
        hours_worked = float(parts[2])
        
        # Calculate total pay
        total_pay = hourly_wage * hours_worked

        # Line information printed
        print(f"{name:<15}{hours_worked:<11}${total_pay:<10.2f}")

    # Closes the file
    f.close()

# Allows the interpreter to read the main method
if __name__ == "__main__":
    main()