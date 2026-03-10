"""
Ciando uma classe 


class Carro: # classe vazia criada
    pass


meu_carro = Carro() # meu_carro agora é um objeto da classe Carro

class Carro: # adicionando atributos( caracteristicas ao objeto)
    
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
    
carro1 = Carro("Toyota", "Preto")
carro2 = Carro("Honda", "Branco")

print(carro1.cor)#  vai printar "Preto" que é a cor atribuída
"""


class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

conta = ContaBancaria("Alexandre", 1000)

conta.depositar(500)

print(conta.saldo)