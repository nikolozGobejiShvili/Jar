class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0
        if self.capacity < 0:
            raise ValueError
        

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        self._size += n
        if self._size > self.capacity:
            raise ValueError
        return self._size

    def withdraw(self, n):
        self._size -= n
        if self._size < 0:
            raise ValueError
        return self._size

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
         self._capacity = capacity
    


    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size
        return self._size

object1=Jar()
print(object1.deposit(10))
print(object1.withdraw(5))
print(object1.capacity)
print(object1)