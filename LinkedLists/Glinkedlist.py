class LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)
   
    def __len__(self):
        i = 0
        node = self.head
        while node:
            i += 1
            node = node.next
        return i
    
    def insertEnd(self,value):
        new_node = Node(value)
        temp = self.head 
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp
        new_node.next = None
        self.tail = new_node


class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)




ll = LL()
node1 = Node(1)
node2 = Node(2)

ll.head = node1
node1.prev = None
node1.next = node2
node2.prev = node1
node2.next = None


ll.insertEnd(3)
print(ll)
print(len(ll))
print([node.value for node in ll])
