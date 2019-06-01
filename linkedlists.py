class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if(self.headval is None):
            self.headval = NewNode
            return
        current = self.headval
        while current.nextval:
            current = current.nextval
        current.nextval = NewNode

list = SLinkedList();
list.headval = Node(1)
e2 = Node(2)
e3 = Node(3)

list.headval.nextval = e2;
e2.nextval = e3;

# list.AtBeginning(5)
#
# list.listprint()

list.AtEnd(50)

list.listprint()



