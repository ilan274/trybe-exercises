# Exercício 3: Modifique o exercício anterior para que as palavras sejam lidas
# de um arquivo. Considere que o arquivo terá cada animal em uma linha.

from random import randint


def random_word_guess():
    with open("./exercise03/lista_animais.txt") as f:
        lines = f.readlines()
    random_word = lines[randint(0, len(lines) - 1)].strip()
    print(f"SECREETT!! the word is {random_word}")
    correct = False
    while not correct:
        guess = input("Adivinha a palavra:\n")
        if random_word.lower() == guess.lower():
            print("Acertou!")
            correct = True
        else:
            print("Errou")


random_word_guess()
