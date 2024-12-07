# Module used to accurately retrieve age from date of birth.
import datetime

"""
Author: Rose McCormack
Version: 7 December 2024
Module: customer.py
Description: This is the customer class representing a customer object for a\n
company called NU Bank. The application will allow us to create loans for customers.
"""

class Customer(object):
    """
    Represents a customer object used to differentiate accounts for withdrawing\n
    loans. The constructor will describe the attributes of the class. 
    """
    def __init__(self, ID: str, firstName: str, lastName: str, email: str, 
                 phoneNumber: str, DOB: datetime.date) -> None:
        """
        Constructor for the customer object. 

        Args:
            ID (str): Identification tag of the customer
            firstName (str): The customer's first name
            lastName (str): The customer's last name
            email (str): The customer's email
            phone (str): The customer's email address
            DOB (date): The customer's date of birth
        """
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email 
        self.phoneNumber = phoneNumber 
        self.DOB = DOB 
    
    def setID(self, ID: str) -> None:
        """
        Sets the identification tag of the customer.

        Args:
            ID (str): The identification tag set for the customer.
        """
        self.ID = ID
    
    def getID(self) -> str:
        """
        Returns the customer's identification tag.

        Return:
            str: The identification tag of the customer.
        """
        return self.ID
    
    def setFirstName(self, firstName: str) -> None:
        """
        Sets the customer's first name.

        Args:
            firstName (str): The first name of the customer.
        """
        self.firstName = firstName

    def getFirstName(self) -> str:
        """
        Returns the customer's first name.

        Return:
            str: The first name of the customer.
        """
        return self.firstName

    def setLastName(self, lastName: str) -> None:
        """
        Sets the customer's last name.

        Args:
            lastName (str): The last name of the customer.
        """
        self.lastName = lastName

    def getLastName(self) -> str: 
        """
        Returns the customer's last name.

        Return:
            str: The last name of the customer.
        """
        return self.lastName
    
    def setEmail(self, email: str) -> None:
        """
        Sets the customer's email.

        Args:
            email (str): The email of the customer.
        """
        self.email = email
    
    def getEmail(self) -> str:
        """
        Returns the customer's email.

        Return:
            str: The email of the customer.
        """
        return self.email

    def setPhoneNumber(self, phoneNumber: str) -> None:
        """
        Sets the customer's phone number.

        Raises:
            ValueError: Raised if the phone number is an improper length\n
            or if the phone number is inputted incorrectly.
        
        Args:
            phoneNumber (str): The phone number of the customer.
        """

        # Debugging logic to get accurate data
        if len(phoneNumber) != 14:
            raise ValueError("Improper length of the phone number.")
        if phoneNumber[0] != '(' or phoneNumber[4] != ')' or phoneNumber[5] != '-' or phoneNumber[9] != '-':
            raise ValueError("Phone number was inputted incorrectly.")
        else:
            self.phoneNumber = phoneNumber
    
    def getPhoneNumber(self) -> str:
        """
        Returns the customer's phone number.

        Return:
            str: The phone number of the customer.
        """
        return self.phoneNumber
    
    def setDOB(self, DOB: str) -> None:
        """
        Sets the customer's date of birth from a string in 'YYYY-MM-DD' format.

        Args:
            DOB (str): A string representing the customer's date of birth.

        Raises:
            ValueError: If DOB is not a valid date string in the format 'YYYY-MM-DD'.
        """

        # Debugging logic to make sure the date input is proper
        try:
            self.DOB = datetime.datetime.strptime(DOB, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("DOB is not a valid date string in the format 'YYYY-MM-DD'.")
    
    def getDOB(self) -> datetime.date:
        """
        Returns the customer's date of birth.

        Return:
            datetime.date: The date of birth of the customer.
        """
        return self.DOB

    def getAge(self) -> int:
        """
        Returns the customer's age.

        Return:
            int: The age of the customer.
        """
        today = datetime.date.today()
        delta = today - self.DOB
        age = int(delta.days / 365.25)
        return age
    
    def isEligible(self) -> bool:
        """
        Returns if the customer is eligible for a loan from NU bank or not.

        Return:
            bool: The loan eligibility of the customer.
        """
        return self.getAge() >= 21

    def str(self) -> str:
        """
        Returns a string representation of the customer object.

        Return:
            str: The string data of the customer. 
        """
        return (
        f"Customer ID:\t{self.ID}\n"
        f"First Name:\t{self.firstName}\n"
        f"Last Name:\t{self.lastName}\n"
        f"Email:\t{self.email}\n"
        f"Phone Number:\t{self.phoneNumber}\n"
        f"Date of Birth (MM/DD/YYYY):\t{self.DOB.strftime('%m/%d/%y')}\n"
        )
