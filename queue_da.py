# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description: Implementation of the Queue ADT class as described in the given specifications.

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def enqueue(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        return

    def dequeue(self) -> object:
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

    # # enqueue example 1
    # q = Queue()
    # print(q)
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)

    # # dequeue example 1
    # q = Queue()
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)
    # for i in range(6):
    #     try:
    #         print(q.dequeue())
    #     except Exception as e:
    #         print("No elements in queue", type(e))

    # # is_empty example 1
    # q = Queue()
    # print(q.is_empty())
    # q.enqueue(10)
    # print(q.is_empty())
    # q.dequeue()
    # print(q.is_empty())

    # # size example 1
    # q = Queue()
    # print(q.size())
    # for value in [1, 2, 3, 4, 5, 6]:
    #     q.enqueue(value)
    # print(q.size())
