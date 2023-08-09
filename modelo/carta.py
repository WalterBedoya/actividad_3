class Carta:
    pinta_constante = ("Corazones", "Diamantes", "Treboles", "Picas")

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

CORAZONES = Carta.pinta_constante[0]
DIAMANTES = Carta.pinta_constante[1]
TREBOLES = Carta.pinta_constante[2]
PICAS = Carta.pinta_constante[3]

carta1 = Carta(9, DIAMANTES)
carta2 = Carta(1, TREBOLES)

print("Carta 1: Valor: " ,carta1.valor," , Pinta: ",carta1.pinta)
print("Carta 1: Valor: " ,carta2.valor," , Pinta: ",carta2.pinta)
