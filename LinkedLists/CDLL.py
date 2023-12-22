class CDLL:
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

    


    

    

class Node:
    def __init__(self, value=None):
        self.prev = None
        self.value = value
        self.next = None

    