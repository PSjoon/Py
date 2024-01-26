class Caneta: 
    
    def __init__(self, cor):
        self._cor = cor
  
    @property
    def cor(self):
        print('PROPERTY COR')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print(valor)
        self.cor = valor
    

caneta = Caneta('Azul')
caneta.cor = 'Rosa'
print(caneta.cor)
