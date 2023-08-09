import random
from punto import Punto

punto_cordenadas=Punto()
punto2_cordenadas=Punto()
punto_cordenadas.modificar_cordenadas(5,4)
punto_cordenadas.imprimir_cordenadas(punto_cordenadas.x,punto_cordenadas.y)
punto_cordenadas.calcular_distancia(punto_cordenadas.x,punto_cordenadas.y,punto2_cordenadas.x,punto2_cordenadas.y)