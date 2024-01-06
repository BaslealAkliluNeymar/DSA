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


   
    
node = AVL(10)
insert(node,5)
insert(node,11)
insert(node,12)
insert(node,10.5)
insert(node,13)
insert(node, 56)
postordertraversal(node)


searchnode(node,156)

