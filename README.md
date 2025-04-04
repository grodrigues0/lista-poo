# Lista de exercícios POO

## Exercício 1: Classe de círculos
Defina uma classe Circle para criar, em um plano cartesiano, um círculo C(O,r) com centro O(a,b) e
raio r.
- O centro O(a,b) é uma tupla.
- Defina um método area() na classe que calcula a área do círculo.
- Defina um método perimetro() na classe que calcula o perímetro do círculo.
- Defina um método test_pertencente(A) na classe que testa se um ponto A(x,y) está dentro
do círculo C(O,r). O ponto A é uma tupla.

## Exercício 2: Classe Dominó
Defina uma classe Domino e instancie objetos que simulam as peças de um jogo de dominó.
- O construtor dessa classe inicializará os valores dos pontos presentes nas duas faces A e B
do dominó (valores padrão 0).
- Defina um método mostrar_pontos() que exibe os pontos de ambos os lados um dominó.
- Defina um método método valor() que retorne a soma dos pontos nas duas faces dos dois
dominós.
- Defina o método __str__() exibe uma tupla dos pontos presentes nas duas faces A e B de
um dominó.

## Exercício 3: Classe de Funcionário
Defina uma classe Funcionario com os seguintes atributos: número de identificação, sobrenome,
nome, data de nascimento, data de admissão, salário.
- Adicione à classe o método idade( ), que retorna a idade do funcionário.
- Adicione à classe o método tempo de casa( ), que retorna o número anos que o funcionário
trabalha na empresa.
- Adicione o método aumento de salario( ) à classe, que aumenta o salário do funcionário
levando em conta o tempo de casa, segundo o pseudocódigo:
- Adicione o método mostrarFuncionario(), que exibe os detalhes funcionário: número
pessoal, sobrenome, nome, idade, antiguidade e salário em euros.

## Exercício 4: Classe Conta Bancária (com acesso restrito aos atributos)
Defina uma classe ContaBancaria para representar uma conta bancária simples.
- O construtor (__init__) deve inicializar privadamente os atributos __saldo e __titular.
- Adicione um método depositar(valor), que aumenta o saldo da conta.
- Adicione um método sacar(valor), que permite sacar dinheiro da conta somente se houver
saldo suficiente.
- Adicione um método exibir_saldo(), que retorna o saldo da conta (getter).
- Use property para criar um getter para o nome do titular e um setter que não permite nomes vazios.
- Defina __str__() para exibir uma representação amigável da conta.

## Exercício 5: Classe Produto (com atributos privados e métodos protegidos)
Crie uma classe Produto para representar um item de uma loja.
- Atributos privados: __nome, __preco e __estoque.
- Método protegido _validar_preco(preco), que verifica se o preço é maior que zero.
- Método alterar_preco(novo_preco), que permite mudar o preço somente se for válido.
- Método vender(quantidade), que reduz o estoque se houver unidades disponíveis.
- Método reabastecer(quantidade), que aumenta o estoque.
- Método exibir_detalhes(), que exibe todas as informações do produto.
- __str__(), para retornar uma string amigável.