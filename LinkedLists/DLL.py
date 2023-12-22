class Node:
    def __init__(self, value=None):
        self.prev = None
        self.value = value
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self,value,location):
        if self.head is None:
            print("Linked List doesnt exist")
        else:
            new_node = Node(value)
            if location == 0:
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
                new_node.prev = None
            elif location == 1:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else: 
                temp = self.head
                for i in range(location):
                    temp = temp.next
                new_node.next = temp.next
                new_node.prev = temp
                new_node.next.prev = new_node
                temp.next = new_node


    def traverseFhead(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            print(temp.value)
    def traverseFtail(self):
        temp = self.tail
        while temp.prev != self.head:
            temp = temp.prev
            print(temp.value)



    def search(self,value):
        if self.head is None:
            print("Doubly Linked List doesn't exist")
        else:
            temp = self.head
            i  = 0
            while temp.next is not None:
                temp = temp.next
                if temp.value == value:
                    print(f"Found the index of the value it is {i - 1} and the value is {temp.value}")
                i+=1




dll = DLL()
node1 = Node(1)
node2 = Node(2)

dll.head = node1
node1.prev = None
node1.next = node2
node2.prev = node1
node2.next = None
dll.tail = node2

dll.insert(23,1)
dll.insert(45,1)
dll.insert(2342,1)
dll.insert(12,1)
dll.insert(00,1)
dll.insert(903,1)
dll.insert(78,1)
dll.insert(54,0)
dll.insert(123131,4)

dll.search(2342)
dll.traverseFhead()
dll.traverseFtail()



print([node.value for node in dll])

