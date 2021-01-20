# Exercício 1: Faça um programa que solicite o nome
# de uma pessoa usuária e imprima-o na vertical.

name = "Ilan"
for char in name:
    print(char)

# Exercício 2: Escreva um programa que receba vários números naturais
# e calcule a soma desses valores. Caso algum valor da entrada seja inválido,
# por exemplo uma letra, uma mensagem deve ser exibida, na saída de erros,
# no seguinte formato: "Erro ao somar valores, {valor} é um valor inválido".
# Ao final, você deve imprimir a soma dos valores válidos.
numbers = "1, 2, s3, 4, 1, 2s".split(", ")

total = 0
for num in numbers:
    if not num.isdigit():
        print(f"Erro ao somar valores, {num} não é um dígito.")
    else:
        total += int(num)
print(total)

try:
    arquivo = open("arquivo.txt", "r")
except OSError:
    # será executado caso haja uma exceção
    print("arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    print("arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally:
    # será sempre executado, independentemente de erro
    print("Tentativa de abrir arquivo")

# Exercício 3: Dado um arquivo contendo estudantes e suas respectivas notas,
# escreva um programa que lê todas essas informações e filtre somente
# as pessoas que estão aprovadas, escrevendo seus nomes em outro arquivo.
# A nota miníma para aprovação é 6.

try:
    file = open("aprovados.txt", "r")
    conteudo = file.readlines()
except OSError:
    print("Uma d")
else:
    aprovados = []
    for line in conteudo:
        nota = int(line.split(" ")[1].split("\n")[0])
        aluno = str(line.split(" ")[0])
        if nota >= 6:
            aprovados.append(aluno)
            aprovados.append("\n")
    file.close()
    file = open("aprovados.txt", "w")
    file.writelines(aprovados)
    file.close()
# seria possível com "with open" também
