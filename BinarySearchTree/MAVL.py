
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


class AVL:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.rigth = None
        self.height = 1

    def __str__(self):
        if self.left is not None:
            return str(self.left.value)
        elif self.rigth is not None:
            return str(self.rigth.value)
        return str(self.value)
    

def insert(node,value):
    if not node:
        node.value = value
    else:
        if node.value > value:
            new_node = AVL(value)
            if node.left is None:
                node.left = new_node
            else:
                insert(node.left ,value)
        else:
            new_node = AVL(value)
            if node.rigth is None:
                node.rigth = new_node
            else:
                insert(node.rigth ,value)

        
def get_height(node):
    if node is None:
        return 0
    return  1 + max(get_height(node.left),get_height(node.rigth))

def get_balance(node):
    if not node:
        return 0
    return (get_height(node.rigth) - 1) - (get_height(node.left) - 1)

def imp_height(node):
    if not node:
        return 
    return node.height == (get_height(node) - 1)

def searchnode(node,value):
    if not node:
        return "Ain't Nothin!"
    else:
        if node.value > value:
            if node.value == value:
                print('Found left it!')
            else:
                searchnode(node.left,value)
        else:
            if node.value == value:
                print('Found rigth it!')
            else:
                searchnode(node.rigth,value)
        


def Inordertraversal(node):
    if not node:
        return 
    else:
        Inordertraversal(node.left)
        print(node.value)
        Inordertraversal(node.rigth)

def preordertraversal(node):
    if not node:
        return 
    print(node.value)
    preordertraversal(node.left)
    preordertraversal(node.rigth)

def postordertraversal(node):
    if not node:
        return 
    postordertraversal(node.left)
    postordertraversal(node.rigth)
    print(node.value)

           

def levelordertraversal(node):
    
node = AVL(70)
insert(node,50)
insert(node,90)
insert(node,30)
insert(node,60)
insert(node,80)
insert(node, 100)
insert(node, 20)
insert(node, 40)
print(levelordertraversal(node))


