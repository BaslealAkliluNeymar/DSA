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




