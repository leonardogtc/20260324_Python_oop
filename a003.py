# Escopo de classe e de método da classe
# O escopo de classe é o contexto em que os atributos e métodos
# de uma classe são definidos. O escopo de método da classe é o
# contexto dentro de um método de classe, onde as variáveis locais
# e os parâmetros são definidos. O escopo de classe é acessível a
# todos os métodos da classe, enquanto o escopo de método é acessível
# apenas dentro do método em que foi definido. Por exemplo, podemos definir um atributo de classe para contar o número de instâncias criadas:
class Pessoa:
    contador = 0  # Atributo de classe

    def __init__(self, nome):
        self.nome = nome
        Pessoa.contador += 1  # Acessando o atributo de classe

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}...'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)  # Chamando outro método da classe


p1 = Pessoa('Alice')
p2 = Pessoa('Bob')

print(f'Número de pessoas criadas: {Pessoa.contador}')

p1.comendo('maçã')
print(p2.comendo('banana'))
print(p1.executar('laranja'))
