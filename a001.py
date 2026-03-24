'''
Classes são tipos de dados definidos pelo usuário. Eles permitem criar objetos personalizados com atributos e métodos específicos. Em Python, tudo é um objeto, incluindo tipos de dados básicos como strings, listas e dicionários.
Em suma, classes são molder para criar novos tipos de dados, enquanto objetos são instâncias desses tipos de dados. Por exemplo, a string 'Leonardo' é um objeto do tipo str, que é uma classe embutida em Python. A classe str define os métodos e atributos que podem ser usados com objetos do tipo string.
CamelCase é uma convenção de nomenclatura onde as palavras são unidas sem espaços, e cada palavra começa com uma letra maiúscula. Em Python, é comum usar CamelCase para nomear classes, como por exemplo: MinhaClasse, Pessoa, Carro, etc.
Para criar uma classe em Python, usamos a palavra-chave 'class' seguida pelo nome da classe. Dentro da classe, podemos definir métodos (funções) e atributos (variáveis) que pertencem à classe. Por exemplo:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.'
'''


class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


p1 = Pessoa('Leonardo', 'Silva', 22)
p2 = Pessoa('Maria', 'Santos', 30)

print(p1)
print(p1.nome)
print(p1.idade)

print(p2)
print(p2.nome)
print(p2.idade)
