# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 2, Dynamic Array
# Description:


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = [None] * self.capacity

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/"+ str(self.capacity)
        out += " " + str(self.data[:self.size])
        return out

    def resize(self, new_capacity: int) -> None:
        """
        If given valid input, sets a new storage list to the data attribute
        of the given capacity containing the same elements in the same index
        """
        # Guard against new_capacity being zero or less than current size
        if (new_capacity == 0) or (new_capacity < self.size):
            return

        # Initialize a new list with capacity of new_capacity
        new_data = [None] * new_capacity

        # Copy data to the new list
        for i in range(self.size):
            new_data[i] = self.data[i]

        # Set the new capacity and data
        self.capacity = new_capacity
        self.data     = new_data

        return

    def append(self, value: object) -> None:
        """
        Adds the given value to the next available index in the data
        attribute, doubling it's capacity if full
        """
        # Check if storage is full and double capacity if true
        if self.is_full():
            self.resize(self.capacity * 2)

        # Set value to next open index and increment size
        self.data[self.size] = value
        self.size += 1

        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        If valid index given, inserts the given value into the data
        attribute list at the given index, shifting existing values
        one index higher if necessary, and doubling the data attribute
        list capacity if it is full.  Raises a DynamicArrayException
        if invalid index value given.
        """
        # Guard against invalid index
        if (index < 0) or (index > self.size):
            raise DynamicArrayException

        # Check if storage is full and double capacity if true
        if self.is_full():
            self.resize(self.size * 2)

        # Shift elements to make room at index for the new value.
        # This is a noop if index is appending to the end of the
        # current data attribute list
        for current_index in range(self.size, index, -1):
            self.data[current_index] = self.data[current_index - 1]

        # Set value at the given index and increment size
        self.data[index] = value
        self.size       += 1

        return

    def get_at_index(self, index: int) -> object:
        """
        If valid index given, returns object at the given index
        in the data attribute list. If invalid index is given,
        raises a DynamicArrayException
        """
        # Guard against invalid index
        if (index < 0) or (index > self.size - 1):
            raise DynamicArrayException

        # Return the value at the given index
        return self.data[index]

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        return

    def is_empty(self) -> bool:
        """
        TODO: Write this implementation
        """
        return False

    def length(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0

    def slice(self, start_index: int, quantity: int) -> object:
        """
        TODO: Write this implementation
        """
        return DynamicArray()

    def reverse(self) -> None:
        """
        TODO: Write this implementation
        """
        return

    def sort(self) -> None:
        """
        TODO: Write this implementation
        """
        return

    def merge(self, another_list: object) -> None:
        """
        TODO: Write this implementation
        """
        return

    def is_full(self) -> bool:
        """
        Returns True if the data attribute has no free space,
        False if there is free space remaining
        """
        if self.size == self.capacity:
            return True

        return False





# BASIC TESTING
if __name__ == "__main__":
    pass

    # # resize - example 1
    # da = DynamicArray()
    # print(da.size, da.capacity, da.data)
    # da.resize(10)
    # print(da.size, da.capacity, da.data)
    # da.resize(2)
    # print(da.size, da.capacity, da.data)
    # da.resize(0)
    # print(da.size, da.capacity, da.data)

    # # resize - example 2
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    # print(da)
    # da.resize(20)
    # print(da)
    # da.resize(4)
    # print(da)

    # # append - example 1
    # da = DynamicArray()
    # print(da.size, da.capacity, da.data)
    # da.append(1)
    # print(da.size, da.capacity, da.data)
    # print(da)

    # # append - example 2
    # da = DynamicArray()
    # for i in range(9):
    #     da.append(i + 101)
    #     print(da)
    #
    # # append - example 3
    # da = DynamicArray()
    # for i in range(600):
    #     da.append(i)
    # print(da.size)
    # print(da.capacity)

    # # insert_at_index - example 1
    # da = DynamicArray([100])
    # print(da)
    # da.insert_at_index(0, 200)
    # da.insert_at_index(0, 300)
    # da.insert_at_index(0, 400)
    # print(da)
    # da.insert_at_index(3, 500)
    # print(da)
    # da.insert_at_index(1, 600)
    # print(da)

    # # insert_at_index example 2
    # da = DynamicArray()
    # try:
    #     da.insert_at_index(-1, 100)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # da.insert_at_index(0, 200)
    # try:
    #     da.insert_at_index(2, 300)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # print(da)

    # # insert at index example 3
    # da = DynamicArray()
    # for i in range(1, 10):
    #     index, value = i - 4, i * 10
    #     try:
    #         da.insert_at_index(index, value)
    #     except Exception as e:
    #         print("Can not insert value", value, "at index", index)
    # print(da)

    # # get_at_index - example 1
    # da = DynamicArray([10, 20, 30, 40, 50])
    # print(da)
    # for i in range(4, -1, -1):
    #     print(da.get_at_index(i))

    # # get_at_index example 2
    # da = DynamicArray([100, 200, 300, 400, 500])
    # print(da)
    # for i in range(-1, 7):
    #     try:
    #         print("Index", i, ": value", da.get_at_index(i))
    #     except Exception as e:
    #         print("Index", i, ": exception occured")

    # # remove_at_index - example 1
    # da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    # print(da)
    # da.remove_at_index(0)
    # print(da)
    # da.remove_at_index(6)
    # print(da)
    # da.remove_at_index(2)
    # print(da)

    # # remove_at_index - example 2
    # da = DynamicArray([1024])
    # print(da)
    # for i in range(17):
    #     da.insert_at_index(i, i)
    # print(da.size, da.capacity)
    # for i in range(16, -1, -1):
    #     da.remove_at_index(0)
    # print(da)

    # # remove_at_index - example 3
    # da = DynamicArray()
    # print(da.size, da.capacity)
    # [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    # print(da.size, da.capacity)
    # [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                      # step 3 - remove 1 element
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 4 - remove 1 element
    # print(da.size, da.capacity)
    # [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 6 - remove 1 element
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 7 - remove 1 element
    # print(da.size, da.capacity)
    #
    # for i in range(14):
    #     print("Before remove_at_index(): ", da.size, da.capacity, end="")
    #     da.remove_at_index(0)
    #     print(" After remove_at_index(): ", da.size, da.capacity)

    # # is_empty - example 1
    # da = DynamicArray()
    # print(da.is_empty(), da)
    # da.append(100)
    # print(da.is_empty(), da)
    # da.remove_at_index(0)
    # print(da.is_empty(), da)

    # # length - example 1
    # da = DynamicArray()
    # print(da.length())
    # for i in range(10000):
    #     da.append(i)
    # print(da.length())
    # for i in range(9999, 5000, -1):
    #     da.remove_at_index(i)
    # print(da.length())

    # # slice example 1
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # da_slice = da.slice(1, 3)
    # print(da, da_slice, sep="\n")
    # da_slice.remove_at_index(0)
    # print(da, da_slice, sep="\n")

    # slice example 2
    # da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    # print("SOUCE:", da)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3)]
    # for i, cnt in slices:
    #     print("Slice", i, "/", cnt, end="")
    #     try:
    #         print(" --- OK: ", da.slice(i, cnt))
    #     except:
    #         print(" --- exception occurred.")

    # # merge example 1
    # da = DynamicArray([1, 2, 3, 4, 5])
    # da2 = DynamicArray([10, 11, 12, 13])
    # print(da)
    # da.merge(da2)
    # print(da)

    # merge example 2
    # da = DynamicArray([1, 2, 3])
    # da2 = DynamicArray()
    # da3 = DynamicArray()
    # da.merge(da2)
    # print(da)
    # da2.merge(da3)
    # print(da2)
    # da3.merge(da)
    # print(da3)

    # # reverse example 1
    # da = DynamicArray([4, 5, 6, 7, 8, 9])
    # print(da)
    # da.reverse()
    # print(da)
    # da.reverse()
    # print(da)

    # # reverse example 2
    # da = DynamicArray()
    # da.reverse()
    # print(da)
    # da.append(100)
    # da.reverse()
    # print(da)

    # # sort example 1
    # da = DynamicArray([1, 10, 2, 20, 3, 30, 4, 40, 5])
    # print(da)
    # da.sort()
    # print(da)
