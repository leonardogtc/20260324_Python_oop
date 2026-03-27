# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json
CAMINHO_ARQUIVO = 'dados.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Alice', 12)
p2 = Pessoa('Bob', 25)
p3 = Pessoa('Charlie', 30)

dados = [vars(p1), vars(p2), vars(p3)]


with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(dados, arquivo)

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)

pessoas = [Pessoa(**dado) for dado in dados]

for pessoa in pessoas:
    print(pessoa.nome, pessoa.idade)
