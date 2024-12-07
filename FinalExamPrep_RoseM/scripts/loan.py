from customer import Customer

"""
Author: Rose McCormack
Version: 7 December 2024
Module: loan.py
Description: This is the class that will represent the loan object. This class\n
will also inherit the Customer object to add to the account.
"""

class Loan(Customer):
    """
    Represents a loan object that a customer object is associated with. The \n
    constructor will describe the attributes of the class.
    """
    def __init__(self, ID: str, agentName: str, amount: float, 
                 interestRate: float, customer: Customer) -> None:
        """
        Constructor for the loan object.

        Args:
            ID (str): The identification tag of the loan.
            agentName (str): The NU Bank loan agent's name.
            amount (float): The total amount of the loan.
            interestRate (float): The loan's interest rate.
            customer (Customer): The customer associated with the loan.
        """
        self.ID = ID
        self.agentName = agentName
        self.amount = amount 
        self.interestRate = interestRate 
        self.customer = customer