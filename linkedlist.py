class node:
    def __init__(self, data,addr=None):
        self.data = data
        self.addr = addr
        
class list:
    def __init__(self,first):
        self.first = first
    def Addfirst(self,data):
        if self.first == None:
            newnode = node(data,None)
            self.first = newnode
        elif self.first != None:
            newnode = node(data)
            newnode.next = self.first
            self.first = newnode
        
        
        
L = list(None)
L.Addfirst(2)
L.Addfirst(1)