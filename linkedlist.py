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
            newnode.addr = self.first
            self.first = newnode
    def AddLast(self,data):
        itr = self.first
        while True:
            if itr.addr != None:
                itr = itr.addr
            else:
                break
        newnode = node(data)
        itr.addr = newnode
    def Size(self):
        itr = self.first
        lenght = 1
        while itr.addr != None:
            itr = itr.addr
            lenght += 1
        return lenght
    def GetFirst(self):
        return self.first.data
        
        
L = list(None)
L.Addfirst(2)
L.Addfirst(1)
L.AddLast(3)
L.AddLast(4)
print(L.GetFirst())