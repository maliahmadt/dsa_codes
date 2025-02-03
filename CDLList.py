class DLList:
    def __init__(self):
        self.sentinal = Node(63)
        self.sentinal.p = self.sentinal 
        self.sentinal.n = self.sentinal 
    def addFirst(self,d):
        if self.sentinal.p == self.sentinal.n:
            newnode = Node(d)
            newnode.p = self.sentinal
            self.sentinal.n = newnode
            newnode.n = self.sentinal
        else:
            newnode = Node(d)
            newnode.n = self.sentinal.n
            newnode.n.p = newnode
            self.sentinal.n = newnode
            newnode.p = self.sentinal
        
        
class Node:
    def __init__(self,d,p=None,n=None):
            self.p = p
            self.d = d
            self.n = n
            
y = DLList()
y.addFirst(3)
y.addFirst(2)
y.addFirst(1)