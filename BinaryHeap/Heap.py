class Heap:
    def __init__(self,size):
        self.customlist = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def peek(node):
    if not node:
        return 
    return node.customlist[1]

def size(node):
    if not node:
        return 
    else:
        return node.heapSize
    
def levelordertraversal(node):
    if not node:
        return 
    else:
        for i in range(node.heapSize + 1):
            print(node.customlist[i])
    
h = Heap(3)
print(size(h))

