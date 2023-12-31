class BST:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return f"{self.value} {self.left} {self.right}"

def insert(root, value):
    if root.value is None:
        root.value = value
    elif value < root.value:
        if root.left is None:
            root.left = BST(value) 
        else:
            insert(root.left,value)     
    else:
        if root.right is None:
            root.right = BST(value)
        else:
            insert(root.right,value)
    
    return "Node Succesfully Added!"


def preordertraverse(root):
    if root is None:
        return
    else:
        print(root.value)
        preordertraverse(root.left)
        preordertraverse(root.right)


def Inordertraversal(root):
    if root is None:
        return 
    else:
        Inordertraversal(root.left)
        print(root.value)
        Inordertraversal(root.right)

def postorderetraversal(root):
    if root is None:
        return 
    else:
        postorderetraversal(root.left)
        postorderetraversal(root.right)
        print(root.value)

def search(root,value):
    if root.value == value:
        print(f"Found it!{root.value}")
    elif value < root.value:
        if root.left.value == value:
            print(f"Found it {root.left.value}")
        else:
            search(root.left,value)
    else:
        if root.right.value == value:
            print("found it")
        else:
            search(root.right,value)
     


newTree = BST(None)
insert(newTree,70)
insert(newTree,50)
insert(newTree,90)
insert(newTree,30)
insert(newTree,60)
insert(newTree,80)
insert(newTree,100)
insert(newTree,20)
insert(newTree,40)


search(newTree, 30)
