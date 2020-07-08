# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 2, Stack ADT
# Description: Implementation of the Stack ADT class as described in the given specifications.

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def push(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        return

    def pop(self) -> object:
        """
        TODO: Write this implementation
        """
        return None

    def top(self) -> object:
        """
        TODO: Write this implementation
        """
        return None

    def is_empty(self) -> bool:
        """
        TODO: Write this implementation
        """
        return False

    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0




# BASIC TESTING
if __name__ == "__main__":
    pass

    # # push example 1
    # s = Stack()
    # print(s)
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    # print(s)

    # # pop example 1
    # s = Stack()
    # try:
    #     print(s.pop())
    # except Exception as e:
    #     print("Exception:", type(e))
    #
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    #
    # for i in range(6):
    #     try:
    #         print(s.pop())
    #     except Exception as e:
    #         print("Exception:", type(e))

    # # top example 1
    # s = Stack()
    # try:
    #     s.top()
    # except Exception as e:
    #     print("No elements in stack", type(e))
    # s.push(10)
    # s.push(20)
    # print(s)
    # print(s.top())
    # print(s.top())
    # print(s)

    # # is_empty example 1
    # s = Stack()
    # print(s.is_empty())
    # s.push(10)
    # print(s.is_empty())
    # s.pop()
    # print(s.is_empty())

    # # size example 1
    # s = Stack()
    # print(s.size())
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    # print(s.size())
