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
