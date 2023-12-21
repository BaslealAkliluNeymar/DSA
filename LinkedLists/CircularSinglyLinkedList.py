class Clinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def CreateClist(self,value):
        new_node = Node(value)
        new_node.next  = new_node
        self.head = new_node
        self.tail = new_node

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

