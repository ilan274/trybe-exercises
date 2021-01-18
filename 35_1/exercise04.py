# Exercício 4: Crie uma função que receba uma lista de nomes e retorne
# o nome com a maior quantidade de caracteres. Por exemplo, para
# ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] ,
# o retorno deve ser "Fernanda" .


def biggest_name(names):
    biggest = 0
    for name in names:
        if len(name) > biggest:
            biggest = len(name)
    return biggest
