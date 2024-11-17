# Statistics module used for calculations
import statistics

"""
Author: Rose McCormack
Module: stats_work.py
Version: 17 November 2024
Description: Create a program to process the file PA7_data.txt. 

             Find the following pieces of information about the file: 
             Number of missing values (-1)
             Number of valid values
             Min
             Max
             Mean
             Standard Deviation. 

             Output your result to the console. 
             Hint: import and use the statistics module
"""

# File parsing and statistics method for descriptive statistics and counts
def filestats(filename):

    # Loop block for repeated input so user does not 
    while True:
        try:
            f = open(filename, 'r')
            print(f"File {filename} opened successfully.")
            print()
            break;
        except FileNotFoundError:
            print(f"The file ${filename} was not found.")
            break
    
    # Variables used for count of N/A values and proper values
    NA_count = 0
    proper_count = 0
    total_vals = []

    # Parsing logic used for summary statistics
    while True:
        try:
            line = f.readline()
            if not line:
                break
            num = float(line.strip())
            if num == -1.0:
                NA_count += 1
            else:
                proper_count += 1
                total_vals.append(num)
        except ValueError:
            print(f"Line '{line}'")
    
    # Output of counts and summary statistics
    if proper_count > 0:
        print(f"Missing values: {round(NA_count, 2)}")
        print(f"Valid values: {round(proper_count, 2)}")
        print(f"Min: {round(min(total_vals), 2)}")
        print(f"Max: {round(max(total_vals), 2)}")
        print(f"Mean: {round(statistics.mean(total_vals), 2)}")
        print(f"Standard Deviation: {round(statistics.stdev(total_vals), 2)}")
    else:
        print("One or more values in the file is/are not valid.")
        
# Main method used for user input and function encapsulation
def main():
    filename = input("Input the file you want to do statistics on: ")
    filestats(filename)

# Used for interpreter to execute main method
if __name__ == "__main__":
    main()