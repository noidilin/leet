# Cycle Array

Circular array is a classic array technique that uses modulo to create a circular effect, enabling O(1) insertions and deletions at the array head. Commonly used to implement circular queues and ring buffers.

## Cycle Array Template

```python
class CycleArray:
    def __init__(self, size=1):
        self.size = size
        # Since Python supports directly creating generic arrays, no type conversion is needed
        self.arr = [None] * size
        # start points to the index of the first valid element, inclusive interval
        self.start = 0
        # remember that end is an open interval,
        # that is, end points to the index of the position after the last valid element
        self.end = 0
        self.count = 0

    # automatic resize helper function
    def resize(self, newSize):
        # create a new array
        new_arr = [None] * newSize
        # copy the elements of the old array to the new array
        for i in range(self.count):
            new_arr[i] = self.arr[(self.start + i) % self.size]
        self.arr = new_arr
        # reset start and end pointers
        self.start = 0
        self.end = self.count
        self.size = newSize

    # add an element to the head of the array, time complexity O(1)
    def add_first(self, val):
        # when the array is full, double the size
        if self.is_full():
            self.resize(self.size * 2)
        # since start is an inclusive interval, move left first, then assign value
        self.start = (self.start - 1 + self.size) % self.size
        self.arr[self.start] = val
        self.count += 1

    # remove an element from the head of the array, time complexity O(1)
    def remove_first(self):
        if self.is_empty():
            raise Exception("Array is empty")
        # since start is an inclusive interval, assign value first, then move right
        self.arr[self.start] = None
        self.start = (self.start + 1) % self.size
        self.count -= 1
        # if the number of elements decreases to one-fourth of the original size, halve the array size
        if self.count > 0 and self.count == self.size // 4:
            self.resize(self.size // 2)

    # add an element to the tail of the array, time complexity O(1)
    def add_last(self, val):
        if self.is_full():
            self.resize(self.size * 2)
        # since end is an open interval, assign value first, then move right
        self.arr[self.end] = val
        self.end = (self.end + 1) % self.size
        self.count += 1

    # remove an element from the tail of the array, time complexity O(1)
    def remove_last(self):
        if self.is_empty():
            raise Exception("Array is empty")
        # since end is an open interval, move left first, then assign value
        self.end = (self.end - 1 + self.size) % self.size
        self.arr[self.end] = None
        self.count -= 1
        # shrink size
        if self.count > 0 and self.count == self.size // 4:
            self.resize(self.size // 2)

    # get the head element of the array, time complexity O(1)
    def get_first(self):
        if self.is_empty():
            raise Exception("Array is empty")
        return self.arr[self.start]

    # get the tail element of the array, time complexity O(1)
    def get_last(self):
        if self.is_empty():
            raise Exception("Array is empty")
        # end is an open interval, pointing to the next position, so subtract 1
        return self.arr[(self.end - 1 + self.size) % self.size]

    def is_full(self):
        return self.count == self.size

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0
```

## Leetcode Exercises

- '641. Design Circular Deque'
- '622. Design Circular Queue'
