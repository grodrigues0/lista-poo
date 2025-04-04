
class Domino:
    def __init__(self, esquerda: int, direita: int):
        self.esquerda = esquerda
        self.direita = direita

    @property
    def esquerda(self):
        return self._esquerda
    
    @esquerda.setter
    def esquerda(self, value):
        if value < 0 or value > 6:
            raise ValueError("Valor deve estar entre 0 e 6.")
        self._esquerda = value
    
    @property
    def direita(self):
        return self._direita
    
    @direita.setter
    def direita(self, value):
        if value < 0 or value > 6:
            raise ValueError("Valor deve estar entre 0 e 6.")
        self._direita = value

    def mostrar_pontos(self):
        return f"Lado A: {self.esquerda} | Lado B: {self.direita}"
    
    def valor(self):
        return self.esquerda + self.direita
    
    def __str__(self):
        return f"Dominó ({self.esquerda}, {self.direita})"
    
# -------------------- Testes --------------------

# d1 = Domino(2, 6)
# d2 = Domino(4, 3)

# print(d1.mostrar_pontos())
# print(d2.mostrar_pontos())

# print(f"Total de pontos: {d1.valor() + d2.valor()}")

# print(d1)
