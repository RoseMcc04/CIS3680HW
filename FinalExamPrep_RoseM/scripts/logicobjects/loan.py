from FinalExamPrep_RoseM.scripts.logicobjects.customer import Customer

"""
Author: Rose McCormack
Version: 7 December 2024
Module: loan.py
Description: This is the class that will represent the loan object. This class\n
will also inherit the Customer object to add to the account.
"""

class Loan(Customer):
    """
    Represents a loan object that a customer object is associated with it. The \n
    constructor will describe the attributes of the class.
    """
    def __init__(
            self, 
            ID: str = '', 
            agentName: str = '', 
            amount: float = '', 
            interestRate: float = '', 
            customer: Customer = None
    ) -> None:
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

    def setID(self, ID: str) -> None:
        """
        Sets the identification tag of the loan.

        Args:
            ID (str): The identification tag of the loan.
        """
        self.ID = ID
    
    def getID(self) -> str:
        """
        Returns the identification tag of the loan.

        Return:
            str: The identification tag of the loan.
        """
        return self.ID
    
    def setAgentName(self, agentName: str) -> None:
        """
        Sets the name of the loan agent overseeing the loan.

        Args:
            agentName (str): The name of the loan agent.
        """
        self.agentName = agentName
    
    def getAgentName(self) -> str:
        """
        Returns the name of the loan agent overseeing the loan.

        Return:
            str: The name of the loan agent.
        """
        return self.agentName
    
    def setAmount(self, amount: float) -> None:
        """
        Sets the principal amount of the loan.

        Args:
            amount (float): The principal amount of the loan.
        """
        self.amount = amount
    
    def getAmount(self) -> float:
        """
        Returns the principal amount of the loan.

        Return:
            float: The principal amount of the loan.
        """
        return self.amount
    
    def setInterestRate(self, interestRate: float) -> None:
        """
        Sets the interest rate of the loan.

        Args:
            interestRate (float): The interest rate of the loan.
        """
        self.interestRate = interestRate
    
    def getInterestRate(self) -> float:
        """
        Returns the interest rate of the loan.

        Return:
            float: The interest rate of the loan.
        """
        return self.interestRate
    
    def setCustomer(self, customer: Customer) -> None:
        """
        Sets the customer for the loan object.

        Raises:
            TypeError: Raised if the input is not a Customer object.
        
        Args:
            customer (Customer): The customer associated with the loan.
        """
        if not isinstance(customer, Customer):
            raise TypeError("The customer input is not a Customer object.")
        else:
            self.customer = customer
    
    def getCustomer(self) -> Customer:
        """
        Returns the customer object associated with the loan.

        Return:
            Customer: The customer associated with the loan.
        """
        return self.customer
    
    def calcSimpleInterest(self, amount: float, interestRate: float, time: float) -> float:
        """
        Calculates the simple interest of the loan.

        Args:
            amount (float): The principal amount of the loan.
            interestRate (float): The interest rate of the loan.
            time (int): The duration of the loan.
        
        Return:
            float: The simple interest accrued on the loan.
        """
        return round(amount * interestRate * time, 2)
    
    def calcCompoundInterest(self, amount: float, interestRate: float, time: float) -> float:
        """
        Calculates the compound interest of the loan.

        Args:
            amount (float): The principal amount of the loan.
            interestRate (float): The interest rate of the loan.
            time (int): The duration of the loan.
        
        Return:
            float: The compound interest accrued on the loan.
        """
        return round((amount * (1 + interestRate) ** time) - amount, 2)
    
    def __str__(self) -> str:
        """
        Returns a string representation of the loan object.

        Return:
            str: The string data of the loan.
        """
        return (
            "Loan ID: " + str(self.ID) + "\n" +
            "Agent's Name: " + self.agentName + "\n" +
            "Principal Amount: " + "${:,.2f}".format(self.amount) + "\n" +
            "Interest Rate: " + "{:.2f}%".format(self.interestRate * 100) + "\n" +
            "Customer ID: " + str(self.customer.getID()) + "\n" +
            "First Name: " + self.customer.getFirstName() + "\n" +
            "Last Name: " + self.customer.getLastName() + "\n" +
            "Email: " + self.customer.getEmail() + "\n" +
            "Phone Number: " + self.customer.getPhoneNumber() + "\n" +
            "Date of Birth: " + self.customer.getDOB().strftime('%m/%d/%Y') + "\n"
        )