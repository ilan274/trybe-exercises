# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.


def greatest_number(a, b):
    if a == b:
        return a
    elif a > b:
        return a
    else:
        return b
