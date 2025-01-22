class node:
    def __init__(self, data,addr):
        self.data = data
        self.addr = addr
        
class list:
    def __init__(self,first):
        self.first = first
    def Addfirst(self,data):
        newnode = node(data,None)
        self.first = newnode
        
        
        
L = list(None)
L.Addfirst(5)