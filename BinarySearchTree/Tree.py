class tree:
    def __init__(self,data,children=[]):
        self.data = data
        self.children = children

    def __str__(self,level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self,tree):
        self.children.append(tree)


t = tree("Drinks",[])
cold = tree("Cold",[])
hot = tree("Hot",[])
tea = tree("tea",[])
cola = tree("Cola",[])

hot.addChild(tea)
cold.addChild(cola)
t.addChild(cold)
t.addChild(hot)

print(t)