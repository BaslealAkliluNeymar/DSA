class LL:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
    

class stack:
    def __init__(self):
        self.linkedlist = LL()

    def __str__(self):
        values = [str(x.value) for x in self.linkedlist]
        return '\n'.join(values)
        
    def push(self,value):
        new_node = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = new_node
            new_node.next = None
        else:
            new_node.next = self.linkedlist.head
            self.linkedlist.head = new_node
    
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack!"
        print(self.linkedlist.head)
        self.linkedlist.head = self.linkedlist.head.next
    
    def peek(self):
        if self.linkedlist.head:
            return self.linkedlist.head.value
        else:
            return "Stack is empty"
    
    def delete(self):
        self.linkedlist.head = None

    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
    

customstack = stack()
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)


print(customstack)




            



