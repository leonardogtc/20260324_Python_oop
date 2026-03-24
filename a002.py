# Métodos em instâncias de classe Python
# Métodos são funções definidas dentro de uma classe que operam 
# em instâncias desta classe. Eles permitem que as instâncias 
# realizem ações # ou manipulem seus próprios dados. 
# Por exemplo, podemos adicionar um método à classe
# Pessoa para apresentar as informações da pessoa:

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()
