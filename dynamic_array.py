# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 2, Dynamic Array
# Description: Implementation of the Dynamic Array class as described in the given specifications.


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


def quick_sort_helper(arr: [], low: int, high: int) -> int:
    """
    Sorts elements to the left and the right of the high index and returns a newly sorted index
    """
    # designate highest index as our target element to compare to
    target = arr[high]

    # initialize index to help place elements that are smaller than the target
    index_1 = low - 1

    # iterate through array and sort to the left and right of the target
    for index_2 in range(low, high, 1):
        if arr[index_2] < target:
            index_1 += 1
            temp = arr[index_1]
            arr[index_1] = arr[index_2]
            arr[index_2] = temp

    # place target element to right of final element placed that was less than target
    arr[high] = arr[index_1 + 1]
    arr[index_1 + 1] = target

    # return index of newly sorted target element
    return index_1 + 1


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
        out += str(self.size) + "/" + str(self.capacity)
        out += " " + str(self.data[:self.size])
        return out

    def resize(self, new_capacity: int) -> None:
        """
        If given valid input, sets a new storage list to the data attribute
        of the given capacity containing the same elements in the same index
        """
        # handle case where invalid new_capacity is passed
        if not isinstance(new_capacity, int) or new_capacity < 1:
            return

        # handle case where new_capacity < self.size
        if new_capacity < self.size:
            return

        # create new (larger) list, copy existing data over, reference w/ self.data
        copy_range = 0
        new_data = [None] * new_capacity
        for index in range(self.size):
            new_data[index] = self.data[index]
        self.data = new_data
        self.capacity = new_capacity

        return

    def append(self, value: object) -> None:
        """
        Adds the given value to the next available index in the data
        attribute, doubling it's capacity if full
        """
        if self.size == self.capacity:
            self.resize(self.capacity * 2)

        # add value to next available index in self.data
        self.data[self.size] = value
        self.size += 1

        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        If valid index given, inserts the given value into the data
        attribute list at the given index, shifting existing values
        one index higher if necessary, and doubling the data attribute
        list capacity if it is full.
        """
        # handle case where invalid index is passed
        if index < 0 or index > self.size:
            raise DynamicArrayException

        # handle case where self.size == self.capacity
        if self.size == self.capacity:
            self.resize(self.capacity * 2)

        # shift elements over to make room for new element at specified index
        for num in range(self.size, index - 1, -1):
            self.data[num] = self.data[num - 1]

        # insert value at specified index
        self.data[index] = value
        self.size += 1

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
        Removes object at index passed
        """
        # handle case where invalid index is passed
        if not isinstance(index, int) or index < 0 or index > self.size - 1:
            raise DynamicArrayException

        # handle case where self.capacity requires adjustment
        if self.size < (self.capacity / 4) and self.size * 2 >= 10:
            self.resize(self.size * 2)
        elif self.size < (self.capacity / 4) and self.size * 2 < 10:
            self.resize(10)

        # remove element at specified index via shifting elements
        for elt in range(index, self.size - 1, 1):
            self.data[elt] = self.data[elt + 1]
        self.data[self.size - 1] = None
        self.size -= 1

    def is_empty(self) -> bool:
        """
        Returns boolean indicating whether self.data is empty
        """
        if self.data[0] is None:
            return True
        else:
            return False

    def length(self) -> int:
        """
        Returns number of objects currently stored in DynamicArray
        """
        return self.size

    def slice(self, start_index: int, quantity: int) -> object:
        """
        Returns new DynamicArray initialized based on parameters
        """
        # handle case where start_index argument is invalid
        if not isinstance(start_index, int) or start_index < 0 or start_index > self.size - 1:
            raise DynamicArrayException

        # handle case where combination of start_index and quantity arguments are invalid
        if (start_index + quantity - 1) > self.size - 1:
            raise DynamicArrayException

        # initialize new DynamicArray using slice of current self.data and return to user
        end_index = start_index + quantity
        initializer = [self.data[i] for i in range(start_index, end_index, 1)]
        return DynamicArray(initializer)

    def reverse(self) -> None:
        """
        Reverses the order of the elements/objects in self.dat
        """
        # determine range over which we just swap elements
        swap_range = 0
        if self.size % 2 == 0:
            swap_range = int(self.size / 2)
        else:
            swap_range = int((self.size - 1) / 2)

        # iterate over swap_range and swap elements
        for index in range(swap_range):
            temp = self.data[index]
            self.data[index] = self.data[self.size - index - 1]
            self.data[self.size - index - 1] = temp

    def sort(self) -> None:
        """
        Sorts self.data for DynamicArray object
        """
        # copy non-NoneType elements of self.data into a working list
        working_list = [None] * self.size
        for index in range(self.size):
            working_list[index] = self.data[index]

        # sort working_list and copy sorted elements back into self.data
        self.quick_sort(working_list, 0, self.size - 1)
        for index in range(self.size):
            self.data[index] = working_list[index]

    def quick_sort(self, arr: [], low: int, high: int) -> None:
        """
        Sorts array utilizing quick sort
        """
        # recursively work through list until list is partitioned into single elements (low < high)
        if low < high:
            # use helper function to sort highest index element and return index of that element
            div_index = quick_sort_helper(arr, low, high)

            # recursively call quick_sort() on two sublists to left/right of sorted element
            self.quick_sort(arr, low, div_index - 1)
            self.quick_sort(arr, div_index + 1, high)

    def merge(self, another_list: object) -> None:
        """
        Appends all objects from input DynamicArray to current DA
        """
        # iterate through another_list.data and self.append() to current DA
        for index in range(another_list.size):
            self.append(another_list.data[index])

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
