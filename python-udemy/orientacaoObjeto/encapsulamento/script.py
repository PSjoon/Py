class Acesso: 
    def __init__(self):
        self.public = 'publico'
        self._protected = 'protected'
        self.__private = 'private'
        
    def metodo_publico(self):
        return 'metodo_publico'
    
    def _metodo_protected(self):
        self._metodo_protected()
        print(self._metodo_protected)
        return '_metodo_protected'
    
    def __metodo_private(self):
        self.__metodo_private()
        print('__metodo_private')
        return '__metodo_private'
    

start = Acesso()
print(start.public)