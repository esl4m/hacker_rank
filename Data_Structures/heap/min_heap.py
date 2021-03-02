# https://www.youtube.com/watch?v=hkyzcLkmoBY

class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [0] * capacity
        self.size = 0  # num of elements currently in our heap


    def get_parent_index(self, index):
        return (index - 1) // 2
    
    def get_left_child_index(self, index):
        return (2 * index + 1)

    def get_right_child_index(self, index):
        return (2 * index + 2)


    def has_parent(self, index):
        # return boolean
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    # get the actual data
    def parent(self, index):
        return self.storage[self.get_parent_index(index)]
    
    def left_child(self, index):
        return self.storage[self.get_left_child_index(index)]
    
    def right_child(self, index):
        return self.storage[self.get_right_child_index(index)]

    def is_full(self):
        return self.size == self.capacity


