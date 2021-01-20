# Exercício 1: Faça um programa que receba um nome e
# imprima o mesmo na vertical em escada invertida.


def escada_invertida(nome):
    for i in range(len(nome), 0, -1):
        print(nome[0:i])
