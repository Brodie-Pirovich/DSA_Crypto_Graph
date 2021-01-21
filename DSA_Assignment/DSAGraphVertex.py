class DSAGraphVertex:
    def __init__(self, inValue):
        self.value = inValue
        self.links = []
        self.count = 0

    def getValue(self):
        return self.value

    def addLink(self, value):
        if(self.count == 0):
          self.links.append(value)
          self.count += 1
        else:
            for i in range(self.count): 
                if(self.links[i] == value):
                    return
                else:
                    self.links.append(value)
                    self.count += 1
                    return
   
    def removeLink(self, value):
        self.links.remove(value)
        self.count - 1

    def toSting(self):
        print("\nNode value is: ", self.value.name)
        print("Links: ")
        for i in range(len(self.links)):
            print(self.links[i].value.name)

                