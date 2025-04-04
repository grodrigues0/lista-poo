from datetime import date

class Funcionario():
    def __init__(self, identificacao, sobrenome, nome, nascimento, admissao, salario):
        self.identificacao = identificacao
        self.sobrenome = sobrenome
        self.nome = nome
        self.dia_nascimento, self.mes_nascimento, self.ano_nascimento = (nascimento[0], nascimento[1], nascimento[2])
        self.dia_admissao, self.mes_admissao, self.ano_admissao = (admissao[0], admissao[1], admissao[2])
        self.salario = salario

    def idade(self):
        dia_atual, mes_atual, ano_atual = (date.today().day, date.today().month, date.today().year)
        idade = ano_atual - self.ano_nascimento
        if (mes_atual, dia_atual) < (self.mes_nascimento, self.dia_nascimento):
            idade -= 1
        return idade
    
    def tempo_de_casa(self):
        dia_atual, mes_atual, ano_atual = (date.today().day, date.today().month, date.today().year)
        tempo = ano_atual - self.ano_admissao
        if (mes_atual, dia_atual) < (self.mes_admissao, self.dia_admissao):
            tempo -= 1
        return tempo
    
    def aumento_de_salario(self):
        tempo_de_casa = int(self.tempo_de_casa())
        print(tempo_de_casa)
        if tempo_de_casa < 5:
            self.salario = self.salario * 1.02
        elif tempo_de_casa < 10:
            self.salario = self.salario * 1.05
        else:
            self.salario = self.salario * 1.10
        
        
    def mostrar_funcionario(self):
        return f"Número pessoal: {self.identificacao}\nSobrenome: {self.sobrenome}\nNome: {self.nome}\nIdade: {self.idade()}\nTempo de casa: {self.tempo_de_casa()} anos\nSalário em €: {self.salario:.2f}"
    

# -------------------- Testes --------------------

# agente = Funcionario('007', 'Bond', 'James', (11,11,1970), (7, 4, 1995), 7500)
# agente.aumento_de_salario()
# print(agente.mostrar_funcionario())
