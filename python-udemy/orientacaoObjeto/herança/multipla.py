class A: 
    
    def quem_sou(self):
        print('A')  
    
class B(A):
    pass
    
    # def quem_sou(self):
    #     print('B')  

class C(A): 
    

    def quem_sou(self):
        print('C')  

class D(B, C): 
    pass
    
    # def quem_sou(self):
    #     print('D')  
    

qual_metodo = D()
qual_metodo.quem_sou()
print(D.mro())