# Mantendo estados dentro da classe
# Em Python, as classes podem manter estados usando atributos de instância.
# Esses atributos são definidos dentro do método __init__ e podem ser
# acessados e modificados por outros métodos da classe. Por exemplo, podemos
# criar uma classe Contador que mantém um estado de contagem:
class Contador:
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1
        return self.contador

    def resetar(self):
        self.contador = 0
        return self.contador


c1 = Contador()
c2 = Contador()

print(c1.incrementar())
print(c1.incrementar())
print(c1.incrementar())

print(c2.incrementar())
print(c2.incrementar())

print(c1.resetar())
print(c2.resetar())
print(c1.incrementar())
print(c2.incrementar())


class Camera:
    def __init__(self, modelo):
        self.modelo = modelo
        self.ligada = False

    def ligar(self):
        self.ligada = True
        print(f'{self.modelo} está ligada.')

    def desligar(self):
        self.ligada = False
        print(f'{self.modelo} está desligada.')

    def filmar(self):
        if self.ligada:
            print(f'{self.modelo} está filmando.')
        else:
            print(f'{self.modelo} está desligada. Ligue a câmera para filmar.')

    def para_filmar(self):
        if self.ligada:
            print(f'{self.modelo} parou de filmar.')
        else:
            print(f'{self.modelo} está desligada. '
                  'Ligue a câmera para parar de filmar.')


camera1 = Camera('Canon')
camera1.ligar()
camera1.desligar()
camera1.filmar()
