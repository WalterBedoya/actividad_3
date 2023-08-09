import random
import math


class Punto: 
    def __init__(self):
        self.x=random.randint(1,8)
        self.y=random.randint(1,8)
    def modificar_cordenadas(self,c1,c2):
        self.x=c1
        self.y=c2
    def imprimir_cordenadas(self,c1,c2):
        print("el punto esta ubicado en ", c1,",",c2)
    
    def calcular_distancia(self,x1,y1,x2,y2)
        

def distancia_entre_puntos(x1, y1, x2, y2):
    
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return distancia
        
