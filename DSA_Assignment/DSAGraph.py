import DSALinkedList as list
import DSAListNode as listNode
import DSAGraphVertex as vertex
import DSAQueue as Queue

class DSAGraph:
    def __init__(self):
        self.linkedList = list.DSALinkedList(None)
        self.count = 0

    def getCount(self):
        return count

    def add_node(self, value):
        if(self.find(value) != None):
            #print("Node already exists!")
            return
        else:
            v = vertex.DSAGraphVertex(value)
            self.linkedList.insertFirst(v)
            self.count += 1

    def add_edge(self, value1, value2):
        node1 = self.find(value1)
        node2 = self.find(value2)
        if(node1 == None or node2 == None):
            print("Could not find node!")
            return
        else:
            node1.addLink(node2)
            node2.addLink(node1)

    def find(self, value):
        v = vertex.DSAGraphVertex(value)
        for item in self.linkedList:
            if(item.value == v.value):
                return item

    def clear(self):
        self.count = 0
        for item in self.linkedList:
            item.links = None
            self.linkedList.removeFirst()

    def display(self):
        for node in self.linkedList:
            node.toSting()

    def bfs(self, value):
      print("\nBreadth first search")
      visited = []
      queue = Queue.ShufflingDSAQueue(vertex.DSAGraphVertex)
      node = self.find(value)

      if node not in visited:
         print(node.value)
         visited.append(node)
         queue.enqueue(node)

         while queue:
            s = queue.dequeue()

            for i in range(len(s.links)):
              if s.links[i] not in visited:
                visited.append(s.links[i].value)
                queue.enqueue(s.links[i].value)         

    def dfs(self, value):
        print("\nDepth first search")
        visited = []
        node = self.find(value)

        if node not in visited:
           print(node.value)
           visited.append(node)

           for i in range(len(node.links)):
               print(node.links[i].value)
               visited.append(node.links[i])