import numpy as np

#
#Base Queue class
#
class DSAQueue:
    def __init__(self, dataType):
        self.dataType = dataType
        self.DEFAULT_CAPACITY = 20
        self.count = -1
        self.queue = np.zeros(self.DEFAULT_CAPACITY, dtype=self.dataType)

    def getCount(self):
        return self.count

    def isEmpty(self):
        return self.count == -1

    def isFull(self):
        return self.count == self.DEFAULT_CAPACITY-1

    def enqueue(self,item):
        if self.isFull():
            return False
        else:
            self.count += 1
            self.queue[self.count] = item

    def dequeue(self):
        if self.isEmpty():
            return False
        else:
            dequeued = self.queue[0]
            self.shuffle()
            return dequeued

    def show(self):
        print ('Queue contents are:')
        for i in range(self.count+1):
            print(self.queue[i])

    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.queue[0]

#
#Shuffling Queue class
#
class ShufflingDSAQueue(DSAQueue):
    def __init__(self, datatype):
        DSAQueue.__init__(self, datatype)
        self.count = -1

    def shuffle(self):
        for i in range(1,self.DEFAULT_CAPACITY):
            self.queue[i-1] = self.queue[i]
        self.count -= 1

    def enqueue(self,item):
        if self.isFull():
            print('Queue is full')
            return False
        else:
            self.count += 1
            self.queue[self.count] = item

    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty')
            return False
        else:
            dequeued = self.queue[0]
            self.shuffle()
            return dequeued

    def show(self):
        print ('Queue contents are:')
        for i in range(self.count+1):
            print(self.queue[i])

#
#Circular Queue class
#
class CircularDSAQueue(DSAQueue):
    def __init__(self, datatype):
        DSAQueue.__init__(self, datatype)
        self.count = 0
        self.front = 0
        self.rear = self.DEFAULT_CAPACITY-1

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.DEFAULT_CAPACITY

    def enqueue(self,item):
        if self.isFull():
            print('Queue is full')
            return False
        else:
            self.rear = (self.rear + 1) % self.DEFAULT_CAPACITY
            self.queue[self.rear] = item
            self.count += 1

    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty')
            return 
        else:
            dequeued = self.queue[self.front]
            self.front = (self.front + 1) % self.DEFAULT_CAPACITY
            self.count -= 1
            return dequeued

    def show(self):
        print ('Queue contents are:')
        for i in range(self.count):
            print(self.queue[int((i+self.front)% self.DEFAULT_CAPACITY)])

    def peek(self):
        if self.isEmpty():
            print('Queue is empty')
            return False
        else:
            return self.queue[self.front]

    def bottom(self):
        if self.isEmpty():
            print('Queue is empty')
            return False
        else:
            return self.queue[self.rear]