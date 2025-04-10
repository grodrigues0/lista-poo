class Categoria():
    def __init__(self, nome):
        self.nome = nome

class Avaliacao():
    def __init__(self, cliente, comentario, nota):
        self.__cliente = cliente
        self.__comentario = comentario
        self.__nota = nota

    def __str__(self):
        return f"Cliente: {self.__cliente}, Comentário: {self.__comentario}, Nota: {self.__nota}"

   
class Produto():
    def __init__(self, nome, preco, estoque, categoria):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
        self.__categoria = categoria
        self.__avaliacoes = []

    def _validar_preco(self, preco):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        return preco

    def _alterar_preco(self, novo_preco):
        self.__preco = self._validar_preco(novo_preco)
        
    def vender(self, quantidade):
        if quantidade <= self.__estoque:
            self.__estoque -= quantidade
        else:
            print(f"Estoque insuficiente para vender {quantidade} unidades de {self.__nome}.")

    def reabastecer(self, quantidade):
        self.__estoque += quantidade

    def adicionar_avaliacao(self, cliente, comentario, nota):
        avaliacao = Avaliacao(cliente, comentario, nota)
        self.__avaliacoes.append(avaliacao)

    def exibir_detalhes(self):
        print(f"Nome: {self.__nome}")
        print(f"Preço: {self.__preco:.2f}")
        print(f"Estoque: {self.__estoque}")
        print(f"Categoria: {self.__categoria.nome}")
        print("Avaliações:")
        if len(self.__avaliacoes) > 0:
            for avaliacao in self.__avaliacoes:
                print(avaliacao)

    def __str__(self):
        return f"{self.__nome} - {self.__preco:.2f} - Estoque: {self.__estoque} - Categoria: {self.__categoria.nome}"




class Loja():
    def __init__(self, nome):
        self.__nome = nome
        self.__produtos = []
    
    def adicionar_produto(self, produto):
        self.__produtos.append(produto)
    
    def listar_estoque(self):
        print(f"Estoque da {self.__nome}:")
        for produto in self.__produtos:
            print(produto)
 


categoria1 = Categoria("Eletrônicos")
categoria2 = Categoria("Livros")

produto1 = Produto("Microondas", 750.00, 10, categoria1)
produto2 = Produto("Do mil ao milhão sem cortar o cafézinho", 49.90, 5, categoria2)

loja = Loja("Loja Exemplo")
loja.adicionar_produto(produto1)
loja.adicionar_produto(produto2)

produto1.vender(2)

produto2.reabastecer(3)

produto1.adicionar_avaliacao("Cliente 1", "Ótimo produto!", 5)

loja.listar_estoque()
produto1.exibir_detalhes()