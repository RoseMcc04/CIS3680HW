"""
Author: Rose McCormack
Version: 8 December 2024
Module: Node.py
Description: This is the Node object that will be used for future structures.
"""

class Node(object):
    """
    This is the Node class that will be used to assist in implementing\n
    future data structures for this file. 
    """
    def __init__(self, 
                 data: any = None, 
                 nextNode: 'Node' = None, 
                 prevNode: 'Node' = None
                 ) -> None:
        """
        Constructor that forms a Node object.

        Args:
            data (Any): The data (type or object) that the Node holds.
            nextNode (Node): The next Node in the structure.
            prevNode (Node): The previous Node in the structure.
        """
        self.data = data
        self.nextNode: 'Node' = nextNode
        self.prevNode: 'Node' = prevNode
    
    def setData(self, data: any):
        """
        Sets the data of the Node object.

        Args:
            data (any): The data that the Node holds.
        """
        self.data = data
    
    def getData(self) -> any:
        """
        Returns the data of the Node object.

        Return:
            any: The data that the Node holds.
        """
        return self.data
    
    def setNextNode(self, nextNode: 'Node') -> None:
        """
        Sets the next node in the collection.

        Args:
            nextNode (Node): The next node in the collection.
        """
        self.nextNode = nextNode
    
    def getNextNode(self) -> 'Node':
        """
        Returns the next node in the collection.

        Return:
            Node: The next node in the collection.
        """
        return self.nextNode
    
    def setPrevNode(self, prevNode: 'Node') -> None:
        """
        Sets the previous node in the collection.

        Args:
            prevNode (Node): The previous node in the collection.
        """
        self.prevNode = prevNode
    
    def getPrevNode(self) -> 'Node':
        """
        Returns the previous node in the collection.

        Return:
            Node: The previous node in the collection.
        """
        return self.prevNode
    
    def __str__(self) -> str:
        """
        Returns a string representation of the Node.

        Return:
            str: The string representation of the node.
        """
        return (
            f"Previous Node:\t{self.prevNode.getData()}\n"
            f"Data:\t{self.data}\n"
            f"Next Node:\t{self.nextNode.getData()}\n"
        )