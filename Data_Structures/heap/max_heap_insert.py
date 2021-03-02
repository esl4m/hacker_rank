#!/bin/python3

class MaxHeap:
    def __init__(self):
        self.items = [None]

    # def insert(self, value) -> object:
    def insert(self, value):
        self.items.append(value)
        # for i in range(len(self.items)):
        for i in range(len(self.items), 0, -1):
            # print(self.items)
            try:
                if self.items[i//2] < self.items[i]:
                    self.items[i//2], self.items[i] = self.items[i], self.items[i//2]
                elif self.items[i*2+1] < self.items[i]:
                    self.items[i*2+1], self.items[i] = self.items[i], self.items[i*2+1]
                elif self.items[i*2] < self.items[i]:
                    self.items[i*2], self.items[i] = self.items[i],self.items[i*2]
            except:
                pass
        return MaxHeap

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3]
