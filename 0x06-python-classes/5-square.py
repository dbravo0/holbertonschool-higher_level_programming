#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print('#' * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
