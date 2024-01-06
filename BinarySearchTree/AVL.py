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


def getheight(node):
    if not node:
        return 0
    return node.height

def rightRotate(node):
    new_node = node.left
    node.left = node.left.right
    new_node.right = node
    node.height = 1 + max(getheight(node.left), getheight(node.right))
    new_node.height = 1 + max(getheight(new_node.left),getheight(new_node.right))
    return new_node


def leftRotate(node):
    new_node = node.right
    node.right = node.right.left
    new_node.left = node
    node.height = 1 + max(getheight(node.left), getheight(node.right))
    new_node.height = 1 + max(getheight(new_node.left),getheight(new_node.right))
    return new_node


def getbalance(node):
    if not node:
        return 0
    return getheight(node.left) - getheight(node.right)

def insertnode(node,value):
    if not node:
        return AVLNODE(value)
    else:
        if node.data < value:
            if node.left is None:
                new_node = AVLNODE(node)
                node.left = new_node
            else:
                insertnode(node.left ,value)
        else:
            if node.right is None:
                new_node = AVLNODE(node)
                node.right = new_node
            else:
                insertnode(node.right , value)

        node.height = 1 + max(getheight(node.left),getheight(node.right))
        balance = getbalance(node)

        if balance > 1 and value < node.left.data:
            #LL Condition
            return rightRotate(node)
        if balance > 1 and value > node.left.data:
            #LR Condition
            node.left = leftRotate(node.left)
            return rightRotate(node)
        if balance < -1 and value > node.right.data:
            #RR Condition
            return leftRotate(node)
        if balance < -1 and value < node.right.data:
            node.right = rightRotate(node.right)
            return leftRotate(node)
        return node

        

            

new_node = AVLNODE(5)
insertnode(new_node,10)

levelordertraversal(new_node)
