import random
import os
from art import logo, vs
from game_data import data

def limpar_tela():
    """Com a função os.system limpa o console"""
    os.system("cls")

def verificar_comparacao(resposta, dado_a, dado_b):
    if resposta == "a" and dado_a['follower_count'] > dado_b['follower_count']:
        return True
    elif resposta == 'b' and dado_b['follower_count'] > dado_a['follower_count']:
        return True
    else:
        return False

def jogar():
    limpar_tela()

    # variáveis
    a = {}
    b = {}

    # controle do fluxo do jogo
    acertou = True

    # controle da pontuacao
    pontuacao = 0


    # dado = nome, ocupação, origem
    # selecionar o dado da lista de modo aleatório
    a = random.choice(data)

    while acertou:
        limpar_tela()
        
        # imprimir a logo nome do jogo
        print(logo)

        if pontuacao > 0:
            print(f"Você está certo. Pontuação atual: {pontuacao}.")

        # imprimir: Compare A: (dado)
        print(f"Compare A: {a['name']}, {a['description']}, {a['country']}.\n")

        # imprimir a logo vs
        print(vs)

        # # imprimir: Compare B: (dado)
        # dado = nome, ocupação, origem
        b = random.choice(data)
        # garantir que 'b' nunca será igual a 'a'
        while a == b:
            b = random.choice(data)
        print(f"Contra B: {b['name']}, {b['description']}, {b['country']}.")

        # imprimir: Quem tem mais seguidores: Digite 'A' ou 'B':
        resposta_usuario = input("Quem tem mais seguidores? Digite 'A' ou 'B': ").lower()

        acertou = verificar_comparacao(resposta_usuario, a, b)
        # se errar
        # imprimir: Sinto muito, está errado. Pontuação final: (número de acertos)
        if not acertou:
            print(f"Sinto muito, você está errado. Pontuação final: {pontuacao}")
        # se acertar
        # imprimi: Você está certo. Pontuação atual: (número de acertos)
        else:
            pontuacao += 1            
            a = b

while input("\nVamos jogar HigherLower: Digite 's' para sim ou 'n' para não: ").lower() == 's':
    jogar()

print("Até a próxima!")