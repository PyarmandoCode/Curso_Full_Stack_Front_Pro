class Cajero:
    def __init__(self,saldo_inicial):
        self.saldo=saldo_inicial

    def consultar_saldo(self):
        return self.saldo    
    
    def depositar(self,cantidad):
        if cantidad>0:
            self.saldo +=cantidad
            return f"Deposito exitoso Nuevo Saldo ${self.saldo}"
        else:
            return "La Cantidad de deposito debe ser mayor a cero"
        
    def retirar(self,cantidad):
        if cantidad> 0 and cantidad <=self.saldo:
            self.saldo -=cantidad
            return f"Retiro exitoso Nuevo Saldo ${self.saldo}"
        elif cantidad<=0:
            return "La Cantidad de retiro debe ser mayor a cero"
        else:
            return "Fondos Insuficientes"
        
#Crear una instancia de cajero
cajero=Cajero(1000)        
#Operaciones con el cajero
print("Saldo Actual", cajero.consultar_saldo())
print(cajero.depositar(500))
print(cajero.retirar(200))
print(cajero.retirar(1500))

