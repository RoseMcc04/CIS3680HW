from FinalExamPrep_RoseM.scripts.logicobjects.customer import Customer
from FinalExamPrep_RoseM.scripts.logicobjects.loan import Loan
from datetime import datetime

"""
Author: Rose McCormack
Version: 7 December 2024
Module: app.py
Description: This is the executable file for our new loan processing system.
"""

def main() -> None:
    customer = Customer()
    loan = Loan()

    try:
        cust_ID = input("Enter your customer ID: ")
        customer.setID(cust_ID)

        firstName = input("Enter your first name: ")
        customer.setFirstName(firstName)

        lastName = input("Enter your last name: ")
        customer.setLastName(lastName)

        email = input("Enter your email address: ")
        customer.setEmail(email)

        phoneNumber = input("Enter your phone number (123-456-7890): ")
        customer.setPhoneNumber(phoneNumber)

        # Handle date input and ensure it's valid
        while True:
            try:
                dateOfBirth = input("Enter your date of birth (YYYY-MM-DD): ")
                customer.setDOB(datetime.strptime(dateOfBirth, "%Y-%m-%d"))
                break
            except ValueError:
                print("Invalid date format. Please enter the date in 'YYYY-MM-DD' format.")

        loan.setCustomer(customer)

        loan_ID = input("Enter your loan ID: ")
        loan.setID(loan_ID)

        agentName = input("Enter your loan agent's name: ")
        loan.setAgentName(agentName)

        time = float(input("Enter the current duration of the loan in years: "))

        # Handle loan amount input and ensure it's valid
        while True:
            try:
                amount = float(input("Enter the principal amount of your loan: "))
                if amount < 0:
                    raise ValueError("Amount cannot be negative.")
                loan.setAmount(amount)
                break
            except ValueError as ve:
                print(f"Invalid input: {ve}. Please enter a valid amount.")

        # Handle interest rate input and ensure it's valid
        while True:
            try:
                interestRate = float(input("Enter the interest rate of your loan as followed (i.e. 0.025, 0.1375, etc.): "))
                if interestRate < 0:
                    raise ValueError("Interest rate cannot be negative.")
                loan.setInterestRate(interestRate)
                break
            except ValueError as ve:
                print(f"Invalid input: {ve}. Please enter a valid interest rate.")

        simpleInterest = loan.calcSimpleInterest(loan.getAmount(), loan.getInterestRate(), time)
        compoundInterest = loan.calcCompoundInterest(loan.getAmount(), loan.getInterestRate(), time)

        # Print loan details
        print("\nLoan Information:\n")
        print(str(loan))  # This will print customer and loan info, formatted as per the __str__ methods.

        # Print financial information
        print(f"Loan Totals based on {time} years:\n")
        print(f"Total simple interest: ${round(simpleInterest, 2)}")
        print(f"Total compound interest: ${round(compoundInterest, 2)}")
        print(f"Total loan with simple interest: ${round(amount + simpleInterest, 2)}")
        print(f"Total loan with compound interest: ${round(amount + compoundInterest, 2)}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()