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
            return self.queue.pop()
    
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
    if not node:
        return 
    else:
        q = queue()
        q.Enqueue(node)
        while not q.isEmpty():
            x = q.Dequeue()
            print(x.data)
            if x.left is not None:
                q.Enqueue(x.left)
            if x.right is not None:
                q.Enqueue(x.right)

def searchnode(node,value):
    if node:
        if node.data == value:
            print("Found it!")
        elif value < node.data:
            if node.left is not None and node.left == value:
                searchnode(node.left,value)
        elif value > node.data:
            if node.right is not None:
                searchnode(node.right,value)
        
        

            

new_node = AVLNODE(10)
x = AVLNODE(5)
y = AVLNODE(15)
c = AVLNODE(20)
b = AVLNODE(4)

new_node.left = x
new_node.right = y
x.left = b
x.right = c
searchnode(new_node,19)

