# Atributos de classe e de instância
# -----------------------------------
# Em Python, as classes podem ter atributos de classe e de instância.
# Os atributos de classe são compartilhados por todas as instâncias da
# classe, enquanto os atributos de instância são específicos para cada
# instância. Por exemplo, podemos criar uma classe Pessoa com um
# atributo de classe chamado especie e um atributo de instância
# chamado nome:
class Pessoa:
    ANO_ATUAL = 2026  # Atributo de classe
    especie = 'Homo Sapiens'  # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ANO_ATUAL - self.idade


p1 = Pessoa('Alice', 12)
p2 = Pessoa('Bob', 25)

print(p1.nome)
print(p2.nome)
print(p1.idade)
print(p2.idade)
print(p1.especie)
print(p2.especie)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
