# Exercício 2: Jogo da palavra embaralhada. Desenvolva um jogo em que
# a pessoa usuária tenha que adivinhar uma palavra que será mostrada
# com as letras embaralhadas. O programa terá uma lista de palavras
# e escolherá uma aleatoriamente. O jogador terá três tentativas
# para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela,
# informando se a pessoa ganhou ou perdeu o jogo.

from random import choice


def random_word_guess():
    random_word = choice(["Ilan", "Herbach", "Jacques", "SP", "RJ"])
    print(f"SECREETT!! the word is {random_word}")
    correct = False
    while not correct:
        guess = input("Adivinha a palavra:\n")
        if random_word == guess:
            print("Acertou!")
            correct = True
        else:
            print("Errou")


random_word_guess()
