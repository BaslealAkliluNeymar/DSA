class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list[::-1]
        values = [str(x) for x in values]
        return '\n'.join(values)

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
    
    def push(self, value):
        self.list.append(value)

    
    def pop(self):
        if len(self.list) == 0:
            print("Nothing to pop here!")
        else:
            return self.list.pop()

    def peek(self):
        if len(self.list) == 0:
            print("Nothing to peek here!")
        else:
            return self.list[len(self.list) - 1]
    
    def delete(self):
        self.list = None

customstack = Stack()
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)

print(customstack)

print(customstack)

print(f"I peeked and i found {customstack.peek()}")