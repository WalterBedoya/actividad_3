from circulo import Circulo

centro=(0,1)
radio=6
circulo1=Circulo(centro, radio)

print("el area es: ", circulo1.area())
print("el perimetro es: ", circulo1.perimetro())
punto_a_evaluar=(0,1)
if circulo1.pertenece_el_punto(punto_a_evaluar):
    print("el punto pertenece al circulo")
else:
    print("el punto no pertenece al circulo")
    