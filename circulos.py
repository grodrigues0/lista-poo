import math

class Circulo:
    def __init__(self, centro, r):
        self.a, self.b = centro
        self.radius = r

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radius
    
    def teste_pertencente(self, ponto):
        x, y = ponto
        dist = math.sqrt((x - self.a) ** 2 + (y - self.a) ** 2)
        return dist <= self.radius

# -------------------- Testes --------------------

# c1 = Circle((2, 2), 3)

# print(c1.perimetro())
# print(c1.area())
# print(c1.teste_pertencente((0, 0)))
# print(c1.teste_pertencente((0, -1)))