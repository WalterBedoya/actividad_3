import random
class Punto: 
    def __init__(self):
        self.x=random.randint(1,8)
        self.y=random.randint(1,8)
    def modificar_cordenadas(self,c1,c2):
        self.x=c1
        self.y=c2
    def imprimir_cordenadas(self,c1,c2):
        
