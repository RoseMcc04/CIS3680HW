"""
Author: Rose McCormack
Version: 20 November 2024
Module: student.py
Description: Resources to manage a student's name and test scores.
"""

class Student(object):
    """
    Represents a student and provides accessors and mutators for data access.\n
    The main attributes being tracked are the student's name and the student's grades.

    Attributes:
        name (str): The name of the student.
        scores (list[int]): The most recent grades of the student.
    """

    def __init__(self, name: str, number: int):
        """
        Initializes a Student instance with a name and grades.

        Args:
            name (str): The name of the student.
            grades (list[int]): The most recent grades of the student.
        """
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self) -> str:
        """
        Returns the student's name.

        Return:
            str: The name of the student.
        """
        return self.name
  
    def setScore(self, i: int, score: int):
        """
        Resets the ith score, counting from 1.

        Args:
            i (int): The index of the score the user wants to access.
            score (int): The score that is replacing the initial score being accessed.
        """
        self.scores[i - 1] = score

    def getScore(self, i: int) -> int:
        """
        Returns the ith score, counting from 1.

        Args:
            i (int): The index of the score the user wants to retrieve.
        
        Returns:
            int: The specific score being accessed.
        """
        return self.scores[i - 1]
   
    def getAverage(self) -> float:
        """
        Returns the average score.

        Return:
            float: The average of the scores for a student.
        """
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self) -> int:
        """
        Returns the highest score.

        Return:
            int: The maximum score of the student.
        """
        return max(self.scores)
 
    def __str__(self) -> str:
        """
        Returns the string representation of the student.

        Return:
            str: The string representation of the student object.
        """
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    def __eq__(self, other: object) -> bool:
        """
        Checks if two students are equal to each other as objects. 

        Args:
            other (object): Object being compared to the student object calling the function.
        
        Raises:
            ValueError: Raised if other is not a Student object.
        
        Return:
            bool: The boolean determining if the two objects are equal to each other or not.
        """
        if not isinstance(other, Student):
            raise ValueError("Object is not a student.")
        return self.name == other.name and self.scores == other.scores

    def __lt__(self, other: object) -> bool:
        """
        Checks if the calling object name is less than the input's name.

        Args:
            other (object): Object being compared to the student object calling the function.
        
        Raises:
            ValueError: Raised if other is not a Student object.
        
        Return:
            bool: The boolean determining if the two objects are equal to each other or not.
        """
        if not isinstance(other, Student):
            raise ValueError("Object is not a student.")
        return (self.name < other.name) or (self.name == other.name and self.scores < other.scores)
    
    def __gt__(self, other: object) -> bool:
        """
        Checks if two students are equal to each other as objects. 

        Args:
            other (object): Object being compared to the student object calling the function.
        
        Raises:
            ValueError: Raised if other is not a Student object.
        
        Return:
            bool: The boolean determining if the two objects are equal to each other or not.
        """
        if not isinstance(other, Student):
            raise ValueError("Object is not a student.")
        return (self.name > other.name) or (self.name == other.name and self.scores > other.scores)

def main():
    # """A simple test."""
    # student = Student("Ken", 5)
    # print(str(student))
    # for i in range(1, 6):
    #     student.setScore(i, 100)
    # print(str(student))

    student1 = Student("Robert Sharpe", 7)
    student2 = Student("Robert Sharpe", 5)
    print(student1.__eq__(student2))
    print(student1.__lt__(student2))
    print(student1.__gt__(student2))

if __name__ == "__main__":
    main()


