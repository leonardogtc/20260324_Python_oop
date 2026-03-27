# __dict__ e vars para atributos de instância
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Alice', 12)
p2 = Pessoa('Bob', 25)


dados = p1.__dict__
print(dados)
print(dados['nome'])
print(dados['idade'])

p1 = Pessoa(**dados)
print(p1.nome)
print(p1.idade)


print(p1.__dict__)
print(p2.__dict__)

# A função vars() retorna o __dict__ de um objeto
print(vars(p1))
print(vars(p2))
