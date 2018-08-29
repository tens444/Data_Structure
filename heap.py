class MaxHeap:
    def __init__(self):
        self._elements = [0] * 20
        self._count = 0

    def length(self):
        return self._count
    
    def add(self, value):
        self._elements[self._count] = value
        self._count += 1
        self.siftup(self._count - 1)

    def siftup(self, index):
        if index > 0:
            parent = int((index - 1) / 2)
            if(self._elements[index] > self._elements[parent]):
                self._elements[index], self._elements[parent] = self._elements[parent], self._elements[index]
                self.siftup(parent)
    
    def extract(self):
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self.siftdown(0)
        return value

    def siftdown(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if(left < self._count and self._elements[left] > self._elements[largest]):
            largest = left
        if(right < self._count and self._elements[right] > self._elements[largest]):
            largest = right
        if largest != index:
            self._elements[index], self._elements[largest] = self._elements[largest], self._elements[index]
            self.siftdown(largest)
    
    def display(self):
        print(self._elements[:self._count])

if __name__ == "__main__":
    import random
    L = MaxHeap()
    for r in [random.randint(1, 100) for i in range(10)]:
        L.add(r)
    L.display()
    sorted = []
    for i in range(L.length()):
        sorted.append(L.extract())
    print(sorted)
