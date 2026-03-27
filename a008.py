# Métodos de classe:
# São métodos que operam na classe em si, e não em instâncias específicas.
# Eles são definidos usando o decorador @classmethod e recebem a classe como
# primeiro argumento (geralmente chamado de cls). Métodos de classe são úteis
# para criar métodos que precisam acessar ou modificar o estado da classe, ou
# para criar métodos de fábrica que retornam instâncias da classe.

class Pessoa:
    ano_atual = 2026  # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa.criar_com_50_anos('Helena')
p2 = Pessoa.criar_por_ano_nascimento('João', 1990)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
