class ContaBancaria():
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return
        elif valor > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        else:
            raise ValueError("Valor de saque inválido.")
        
    
    @property
    def exibir_saldo(self):
        print(self.__saldo)
        return f"{self.__saldo:.2f}"
    
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nome):
        if nome != "":
            self.__titular = nome
        else:
            raise ValueError("Nome do titular não pode ser vazio.")
        
    def __str__(self):
        return f"Conta de {self.__titular}\n\n{self.__saldo:.2f}"
        

# -------------------- Testes --------------------
# c1 = ContaBancaria("Alice", 1000)
# print(c1)

# c1.depositar(500)
# print(c1.exibir_saldo)

# c1.sacar(2000)
# c1.sacar(300)

# print(c1.exibir_saldo)
# c1.titular = ""