import random
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head 
            while temp.next is not None:
                temp = temp.next
            
            temp.next = new_node
            new_node.prev = temp
            new_node.next = None
            self.tail = new_node

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def generate(self, n , min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.insertEnd(random.randint(min_value,max_value))
        return self




class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)




ll = LL()
ll.generate(5 ,1, 10)

print(ll)
print(len(ll))
print([node.value for node in ll])
