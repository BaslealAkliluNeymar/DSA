from Queue import Queue
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


q = Queue.queue()

q.Enqueue(1)
q.Enqueue(2)

print(q)


new_node = AVLNODE(10)
x = AVLNODE(15)
y = AVLNODE(5)
new_node.left = y
new_node.right = x
print(postordertraversal(new_node))