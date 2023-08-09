import random
import math

class Rectangulo:
    def __init__(self):
        self.esquina1=(random.randint(1,8),random.randint(1,8))
        self.esquina2=(random.randint(1,8),random.randint(1,8))
        self.esquina3=(random.randint(1,8),random.randint(1,8))
        self.esquina4=(random.randint(1,8),random.randint(1,8))
        
        #aca abajo por si quiere probar si es cuadrado
        #self.esquina1=(4,4)
        #self.esquina2=(4,4)
        #self.esquina3=(4,4)
        #self.esquina4=(4,4)

    def distancia_entre_puntos(self, punto1, punto2):
            
            x1, y1 = punto1
            x2, y2 = punto2
            distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            return distancia

    def calcular_lados(self):
            lado1 = self.distancia_entre_puntos(self.esquina1, self.esquina2)
            lado2 = self.distancia_entre_puntos(self.esquina2, self.esquina3)
            lado3 = self.distancia_entre_puntos(self.esquina3, self.esquina4)
            lado4 = self.distancia_entre_puntos(self.esquina4, self.esquina1)
            return lado1, lado2, lado3, lado4
    
    def area(self):
            
            lado1, lado2, _, _ = self.calcular_lados()
            area = lado1 * lado2

            return area

    def perimetro(self):

        lado1, lado2, lado3, lado4 = self.calcular_lados()
        perimetro = lado1 + lado2 + lado3 + lado4

        return perimetro
    
    def cuadrado(self):

        lado1, lado2, lado3, lado4 = self.calcular_lados()

        return lado1 == lado2 == lado3 == lado4