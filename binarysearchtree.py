class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data

    def findValue(self, data):
        if data < self.val:
            if self.left is None:
                return False
            return self.left.findValue(data)
        elif data > self.val:
            if self.right is None:
                return False
            return self.right.findValue(data)
        else:
            return True



    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val),
        if self.right:
            self.right.PrintTree()



root = Node(1)
root.insert(5)
root.insert(7)
print(root.findValue(5))

root.PrintTree()

