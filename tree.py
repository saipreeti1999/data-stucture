class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def printTree(self):
        print(self.data)
root=node(10)
root.printTree()
