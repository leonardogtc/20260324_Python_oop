from a007 import CAMINHO_ARQUIVO, Pessoa
import json
with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)

pessoas = [Pessoa(**dado) for dado in dados]

for pessoa in pessoas:
    print(pessoa.nome, pessoa.idade)
