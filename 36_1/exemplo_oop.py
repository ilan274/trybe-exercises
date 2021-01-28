# Orientado a objetos: Utiliza objetos para realizar a troca de mensagens
# na aplicação. Como dito anteriormente, objetos são uma estrutura de dados
# mais complexa, que mescla informações e comportamentos.
# Exemplo em Python:


class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.result = 0

    def sum(self):
        self.result = self.n1 + self.n2

    def subtract(self):
        self.result = self.n1 - self.n2

    def multiply(self):
        self.result = self.n1 * self.n2

    def divide(self):
        self.result = self.n1 / self.n2


calc = Calculator(4, 4)
calc.sum()

print("Resultado de 4 + 4:", calc.result)
