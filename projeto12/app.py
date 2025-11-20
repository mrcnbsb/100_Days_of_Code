import random
import os
from art import logo

def limpar_tela():
    os.system("cls")

def jogar():
    limpar_tela()
    print(logo)

    num = random.randint(1, 100)
    tentativas = -1
    acertou = False

    print("Bem-vindo ao Jogo Advinha Número!")
    print("Estou pensando em um número entre 1 e 100.")
    dificuldade = input("Escolha a dificuldade. Digite 'f' para fácil, 'm' para médio ou 'd' para difícil: ").lower()
    if dificuldade == 'f':
        tentativas = 10
    elif dificuldade == 'm':
        tentativas = 7
    elif dificuldade == 'd':
        tentativas = 5
    else:
        print("Escolha inválida!")

    for _ in range(tentativas):
        print(f"\nVocê tem {tentativas} tentativas para advinhar o número.")
        palpite = int(input("Faça um palpite: "))
        if palpite == num:
            acertou = True
            break
        elif palpite < num:
            print("Muito baixo.")
        else:
            print("Muito alto.")
        print("Tente novamente.")
        tentativas -=1

    if acertou:
        print("Você acertou.", end="")
    else:
        print("Você não acertou.", end="")

    print(f" A resposta era {num}.")

while input("\nVamos jogar Advinha Número? Digite 's' para sim ou 'n' para não: ").lower() == "s":
    jogar()

print("Até a próxima!")