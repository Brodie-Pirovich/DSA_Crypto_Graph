import DSAListNode as listNode

class DSALinkedList:
    def __init__(self, head):
        self.head = None

    def insertFirst(self, newValue):
        newNd = listNode.DSAListNode(newValue)
        if(self.isEmpty() == True):
            self.head = newNd
        else:
            newNd.setNext(self.head)
            self.head = newNd

    def insertLast(self, newValue):
        newNd = listNode.DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNd
        else:
            currNd = self.head
            while(currNd.getNext() != None):
                currNd = currNd.getNext()
            currNd.setNext(newNd)

    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False

    def peekFirst(self):
        if(self.isEmpty()):
            return
        else:
            nodeValue = self.head.getValue()
            return nodeValue

    def peekLast(self):
        if(self.isEmpty()):
            return
        else:
            currNd = self.head
            while(currNd.getNext() != None):
                currNd = currNd.getNext()
            nodeValue = currNd.getValue()

    def removeFirst(self):
        if(self.isEmpty()):
            return
        else:
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()

    def removeLast(self):
        if(self.isEmpty()):
            return
        elif(self.head.getNext() == None):
            nodeValue = self.head.getValue()
            self.head = None
        else:
            prevNd = None
            currNd = self.head
            while(currNd.getNext() != None):
                prevNd = currNd
                currNd = currNd.getNext()
            prevNd.setNext(None)
            nodeValue = currNd.getValue()

    def __iter__(self):
        currNd = self.head
        while currNd is not None:
            yield currNd.value
            currNd = currNd.getNext()
