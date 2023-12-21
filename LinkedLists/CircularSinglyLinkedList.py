class Clinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    
    def CreateClist(self, value):
        new_node = Node(value)
        new_node.next  = new_node
        self.head = new_node
        self.tail = new_node
        return "The CLL has been created!"

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

linkedlist = Clinkedlist()
linkedlist.CreateClist(1)

print([node.value for node in linkedlist])
