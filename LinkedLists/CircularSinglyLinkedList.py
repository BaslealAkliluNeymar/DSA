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
    
    def insert(self,value,location):
        if self.head is None:
            print("Linked List Doesnt exist!")
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                 temp = self.head
                 while temp.next is not None:
                     if temp.next == self.head:
                        break    
                     temp = temp.next
                 new_node.next = temp.next
                 temp.next = new_node
                 self.tail = new_node  
            else:
                 temp = self.head
                 for i in range(location - 1):
                     temp = temp.next
                 nextnode = temp.next
                 new_node.next = nextnode
                 temp.next = new_node

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            if temp == self.tail.next:
                break

    def search(self,value):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            if temp == self.tail.next:
                break
            if temp.value == value:
                print('{} is the value i found'.format(temp.value))
            

                    


class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

linkedlist = Clinkedlist()
linkedlist.CreateClist(1)
linkedlist.insert(12,1)
linkedlist.insert(99,1)
linkedlist.insert(99,1)
linkedlist.insert(101,2)
linkedlist.search(12)


print([node.value for node in linkedlist])


linkedlist.traverse()