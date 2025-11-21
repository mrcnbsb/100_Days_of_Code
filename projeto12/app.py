import random
import os
from art import logo

# constantes que definem o número de tentativas conforme o nível escolhido pelo usuário
NIVEL_FACIL = 10
NIVEL_MEDIO = 7
NIVEL_DIFICIL = 5

def limpar_tela():
    os.system("cls")

def definir_dificuldade(opcao):
    if opcao == 'f':
        return NIVEL_FACIL
    elif opcao == 'm':
        return NIVEL_MEDIO
    elif opcao == 'd':
        return NIVEL_DIFICIL
    else:
        return -1

def verificar_palpite(palpite, num):
    if palpite == num:
        return True
    elif palpite < num:
        print("Muito baixo.")
        return False
    else:
        print("Muito alto.")
        return False

def jogar():
    limpar_tela()
    print(logo)

    resposta = random.randint(1, 100)
    acertou = False

    print("Bem-vindo ao Jogo Adivinha Número!")
    print("Estou pensando em um número entre 1 e 100.")
    tentativas = definir_dificuldade(input("Escolha a dificuldade. Digite 'f' para fácil, 'm' para médio ou 'd' para difícil: ").lower())
    if tentativas == -1:
        print("Escolha inválida!")

    for _ in range(tentativas):
        print(f"Você tem {tentativas} tentativas para adivinhar o número.")
        acertou = verificar_palpite(int(input("Faça um palpite: ")), resposta)
        if acertou:
            break
        else:
            print("Tente novamente.")
        tentativas -=1

    if acertou:
        print("Você acertou.", end="")
    else:
        print("Você não acertou.", end="")

    print(f" A resposta era {resposta}.")

while input("Vamos jogar Adivinha Número? Digite 's' para sim ou 'n' para não: ").lower() == "s":
    jogar()

print("Até a próxima!")