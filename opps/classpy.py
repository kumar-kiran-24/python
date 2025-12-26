class A:
    def __init__(self,a,b):#constrocutr
      self.a=a
      self.b=b

    def add(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b
    
    def product(self)->int:
        return self.a*self.b
    
    def div(self):
        return self.a/self.b
    
if __name__ =="__main__":
    obj=A(2,3)
    print("addtion",obj.add())
    print("subtraction",obj.sub())
    print("multiplicatin",obj.product())
    print("divison",obj.div())
    


