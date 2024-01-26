class Caneta: 
    
    def __init__(self, cor):
        self.cor_tinta = cor
        
    # def get_cor(self):
    #     print('GET COR')
    #     return self.cor
    
    @property
    def cor(self):
        print('PROPERTY COR')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 'White'

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)
