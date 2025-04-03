class Domino:
    def __init__(self, esquerda: int, direita: int):
        self.esquerda = esquerda
        self.direita = direita

    def mostrar_pontos(self):
        return f"Lado A: {self.esquerda} | Lado B: {self.direita}"
    
    def valor(self):
        return self.esquerda + self.direita
    
    def __str__(self):
        return f"Dominó ({self.esquerda}, {self.direita})"
    

d1 = Domino(2, 6)
d2 = Domino(4, 3)

print(d1.mostrar_pontos())
print(d2.mostrar_pontos())

print(f"Total de pontos: {d1.valor() + d2.valor()}")

print(d1)
