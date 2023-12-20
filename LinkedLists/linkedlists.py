class linkedList():
    #This is linkedlist class!
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node 
            node = node.next
    def insert(self,value,location):
        new_node = Node(value)
        if linkedList.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == 1:
                new_node= None
                self.tail.next = new_node
                self.tail = new_node
            else:
                tempnode = self.head
                for i in range(location):
                    tempnode = tempnode.next
                nextnode = tempnode.next
                tempnode.next = new_node
                new_node.next = nextnode

                

class Node():
    def __init__(self,value=None):
        self.value = value
        self.next = None
    



linkedlist = linkedList()
node1 = Node(1)
node2 = Node(2)

linkedlist.head = node1
linkedlist.head.next = node2
linkedlist.tail = node2
print([node.value for node in linkedlist])