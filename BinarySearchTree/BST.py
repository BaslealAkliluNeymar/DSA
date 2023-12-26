class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
def insert(rootnode ,value):
    if rootnode.value is None:
        rootnode.value = value
    elif value <= rootnode.value:
        if rootnode.left is None:
            rootnode.left = BST(value)
        else:
           insert(rootnode.left , value)
    else:
        if rootnode.right is None:
            rootnode.right = BST(value)
        else:
            insert(rootnode.right , value)
    return 'Node has been succesfully added!'


           
    
bst = BST(70)
print(insert(bst,60))
print(insert(bst,90))
print(bst.left.value)
print(bst.right.value)
