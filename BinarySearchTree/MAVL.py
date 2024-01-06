class AVL:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.rigth = None

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

node = AVL(10)
insert(node,5)
insert(node,11)
insert(node,12)
insert(node,10.5)
insert(node,13)
insert(node, 56)

print(get_height(node) - 1)
print(get_balance(node.rigth.left))
