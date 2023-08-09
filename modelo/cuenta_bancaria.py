
class CuentaBancaria:

    def __init__(self, numero_cuenta, propietarios, balance):

        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balances = balance

    def depositar(self, cantidad):  
            
            if cantidad > 0:
                self.balances += cantidad
                print("Se depositaron" , cantidad ," pesos. Nuevo saldo: " , self.balances )
            else: 
                ("el monto del depósito debe ser positivo.")
            
    def retirar(self, cantidad):
            
            if 0 < cantidad <= self.balances:
                self.balances -= cantidad
                print("Se retiraron",cantidad," unidades. Nuevo saldo:",self.balances)
            else:
                print("Monto no válido para retiro.")

    def aplicar_cuota_manejo(self):
            
            cuota = self.balances * 0.02
            self.balances -= cuota
            print("Se aplicó una cuota de manejo del 2%. Su saldo actual es: " ,self.balances)

    def mostrar_detalles(self):
        
        print("Detalles de la cuenta bancaria:")
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", self.propietarios)
        print("Balance:", self.balances)



cuenta1 = CuentaBancaria("1234", "Walter", 1500)
print("balance inicial: ",cuenta1.balances)
cuenta1.depositar(300)
cuenta1.retirar(1000)
cuenta1.aplicar_cuota_manejo()
cuenta1.mostrar_detalles()