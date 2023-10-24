#!/usr/bin/python3

"""
This module defines a Square class.
"""

class Square:
    """
    This class defines a square with a private size attribute.
    
    Attributes:
        __size (int): The size of the square.
    """
    
    def __init__(self, size):
        """
        Initializes the square with a given size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
