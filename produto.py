class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    def _validar_preco(self, preco):
        if preco <= 0:
            raise ValueError("Preço deve ser maior que zero.")
        return True
    
    def alterar_preco(self, preco):
        if self._validar_preco(self.__preco):
            self.__preco = preco

    def vender(self, quantidade):
        if quantidade > self.__estoque:
            raise ValueError("Quantidade em estoque insuficiente.")
        self.__estoque -= quantidade
        return True
    
    def reabastecer(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")
        self.__estoque += quantidade
        return True
    
    def exibir_detalhes(self):
        return f"Produto: {self.__nome}\nPreço: {self.__preco:.2f}\nEstoque: {self.__estoque}"
    
    def __str__(self):
        return f"Produto: {self.__nome}\nPreço: {self.__preco:.2f}\nEstoque: {self.__estoque}"
    


# -------------------- Testes --------------------

# p = Produto("Caderno", 15.50, 10)
# print(p)

# # p.alterar_preco(-5)
# p.alterar_preco(20)

# p.vender(5)
# # p.vender(10)

# p.reabastecer(15)
# print(p.exibir_detalhes())
