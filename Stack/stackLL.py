class LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node 
            node = node.next

class Node:
    def __init__(self,value=None):
        self.value = None
        self.next = None


class stack:
    def __init__(self):
        self.linkedlist = LL()
        

    def push(self,value):
        new_node = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = new_node
            new_node.next = None
        else:
            new_node.next = self.head.next
            self.head = new_node
    
    def pop(self):
        print(self.linkedlist.head)
        self.linkedlist.head = self.linkedlist.head.next
    
    def peek(self):
        if self.linkedlist.head:
            return self.linkedlist.head
        return "Stack is empty"
    
    def delete(self):
        self.linkedlist.head = None

    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        return False
    

customstack = stack()
print(customstack.peek())


            



