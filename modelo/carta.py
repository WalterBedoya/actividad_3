class Carta:
    PINTAS = ("Corazones", "Diamantes", "Tréboles", "Picas")

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

CORAZONES = Carta.PINTAS[0]
DIAMANTES = Carta.PINTAS[1]
TRÉBOLES = Carta.PINTAS[2]
PICAS = Carta.PINTAS[3]

carta1 = Carta(10, CORAZONES)
carta2 = Carta(3, PICAS)

print("Carta 1: Valor: " ,carta1.valor," , Pinta: ",carta1.pinta)
print("Carta 1: Valor: " ,carta2.valor," , Pinta: ",carta2.pinta)
