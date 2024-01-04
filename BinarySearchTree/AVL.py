from Queue import myfunc
class queue:
    """
        An Implementation of a Queue Data Structure 
        using python lists.
    """
    def __init__(self):
        self.queue = []

    def __str__(self):
        values = [str(x) for x in self.queue]
        return "\n".join(values)

    def Enqueue(self,value):
        return self.queue.append(value)
    
    def Dequeue(self):
        if len(self.queue) == 0:
            return "Nothing to Dequeue"
        else:
            self.queue.pop()
    
    def peek(self):
        return self.queue[len(self.queue) - 1]
    

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False
    
    def delete(self):
        self.queue = []







class AVLNODE:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data
        self.height = 1


def preordertraverse(node):
    if not node:
        return 
    print(node.data)
    preordertraverse(node.left)
    preordertraverse(node.right)


def Inordertraversal(node):
    if not node:
        return 
    Inordertraversal(node.left)
    print(node.data)
    Inordertraversal(node.right)

def postordertraversal(node):
    if not node:
        return 
    postordertraversal(node.left)
    postordertraversal(node.right)
    print(node.data)

def levelordertraversal(node):
    print(node)

myfunc.deef()