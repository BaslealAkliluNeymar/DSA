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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0: 
                new_node.next = self.head
                self.head = new_node
            elif location == 1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                tempnode = self.head
                for i in range(location):
                    tempnode = tempnode.next
                nextnode = tempnode.next
                tempnode.next = new_node
                new_node.next = nextnode

    def traverse(self):
        if self.head is None:
            print("No Head! No Body! No Existence!")
        else:
            temp = self.head
            while temp.next is not None:
                print(temp.value)
                temp = temp.next

    def search(self,value):
        if self.head is None:
            print("No Head! No Body! No Existence")
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
                if temp.value == value:
                    print(f'This is what i found {temp.value}')
            else:
                print("I didn't find anything!")
        
    def delete(self,location):
        if self.head is None:
            print("No Head! No Body! No Existence!") 
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    temp = self.head
                    while temp.next is not None:
                        if temp.next == self.tail:
                            self.tail = temp
                            temp.next = None
                        temp = temp.next
            else:
                temp = self.head
                for i in range(location):
                    temp = temp.next
                nextnode = temp.next
                temp.next = nextnode.next


    def Print(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            print(temp.value)
                


            
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


linkedlist.insert(2,1)
linkedlist.insert(3,1)
linkedlist.insert(4,1)
linkedlist.insert(4,0)
linkedlist.insert(4,3)

print([node.value for node in linkedlist])
linkedlist.traverse()
linkedlist.search(5)
linkedlist.delete(1)
linkedlist.Print()