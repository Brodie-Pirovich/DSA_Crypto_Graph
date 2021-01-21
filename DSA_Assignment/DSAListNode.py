
class DSAListNode:
    def __init__(self, inValue):
        self.value = inValue
        self.next = None

    def getValue(self):
        return self.value

    def setValue(self, inValue):
        value = inValue

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext