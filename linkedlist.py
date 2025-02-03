class node:
    def __init__(self, data,addr=None):
        self.data = data
        self.addr = addr
        
class SLList:
    def __init__(self,first):
        self.first = first
    
    def Addfirst(self,data):
            if self.first == None:
                self.first = node(data)
            else:
                new_node = node(data)
                new_node.addr = self.first
                self.first = new_node
                
    def Addlast(self,data):
        current = self.first
        while current.addr != None:
            if current.addr != None:
                current = current.addr
        new_node = node(data)
        current.addr = new_node
                
p = SLList(None)
p.Addfirst(2)
p.Addfirst(1)
p.Addlast(3)
p.Addlast(4)
p.Addlast(5)
p.Addlast(6)