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



def traverse(rootnode):
    if not rootnode:
        return 
    else:
        print(rootnode.value)
        traverse(rootnode.left)
        traverse(rootnode.right)

def inordertraveral(rootnode):
    if not rootnode:
        return
    else:
        inordertraveral(rootnode.left)
        print(rootnode.value)
        inordertraveral(rootnode.right)
def postordertraversal(rootnode):
    if not rootnode:
        return
    else:
        postordertraversal(rootnode.right)
        print(rootnode.value)
        postordertraversal(rootnode.left)
     
           
    
bst = BST(70)
insert(bst,90)
insert(bst,50)
insert(bst,30)
insert(bst,60)
insert(bst,20)
insert(bst,40)
insert(bst,80)
insert(bst,100)


postordertraversal(bst)