from rectangulo import Rectangulo

rectangulo1=Rectangulo()
print("el area es: ", rectangulo1.area())
print("el perimetro es: ", rectangulo1.perimetro())
print(rectangulo1.esquina1)
print(rectangulo1.esquina2)
print(rectangulo1.esquina3)
print(rectangulo1.esquina4)
if rectangulo1.cuadrado():
    print("es cuadrado")
else:
    print("no es cuadrado")