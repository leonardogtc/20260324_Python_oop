# Métodos estáticos (@staticmethod):
# São métodos que não dependem da instância ou da classe. Eles são definidos
# usando o decorador @staticmethod e não recebem nenhum argumento especial
# (nem self nem cls). Métodos estáticos são úteis para criar funções que estão
# relacionadas à classe, mas não precisam acessar ou modificar o estado da
# classe ou de suas instâncias.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18


p1 = Pessoa('Helena', 50)
print(Pessoa.e_maior_de_idade(p1.idade))
print(Pessoa.e_maior_de_idade(12))
