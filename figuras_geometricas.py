from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        super().__init__("Círculo")
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.raio
    
class Retangulo(FiguraGeometrica):
    def __init__(self, largura, altura):
        super().__init__("Retângulo")
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Triângulo")
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + 2 * math.sqrt((self.base / 2) ** 2 + self.altura ** 2)
    

circulo = Circulo(5)
retangulo = Retangulo(4, 6)
triangulo = Triangulo(3, 4)
figuras = [circulo, retangulo, triangulo]
for i in range(len(figuras)):
    figura = figuras[i]
    print(f"Nome: {figura.nome}")
    print(f"Área: {figura.area():.2f}")
    print(f"Perímetro: {figura.perimetro():.2f}\n")

