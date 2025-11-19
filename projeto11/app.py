import random
import os
from art import logo


def limpar_tela():
    os.system("cls")


def exibir_maos(msg):
    print(f"Sua mão final: {suas_cartas}, pontuação final: {sum(suas_cartas)}")
    print(
        f"Mão final da mesa: {pc_cartas}, pontuação final: {sum(pc_cartas)} ")
    print(msg)


def fazer_blackjack(cartas):
    """Função que verifica se a soma das cartas é igual a 21"""
    if sum(cartas) == 21:
        return True
    else:
        return False

# Ás = 11 ou 1
# Valete, Dama e Rei = 10
# 2 = 2, 3 = 3, ..., 10 = 10


# lista com as cartas para sorteio com a random.choice
cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# controle do fluxo do jogo
quero_jogar = True

limpar_tela()

while quero_jogar:
    print(logo)

    # verifica se o usuário quer jogar Blackjack
    op1 = input("Você quer jogar Blackjack? Digite 's' ou 'n': ").lower()

    # caso o usuário queira jogar
    if op1 == 's':
        # limpa a tela com os.system('cls')
        limpar_tela()

        # lista com duas cartas iniciais do usuário
        suas_cartas = [random.choice(cartas), random.choice(cartas)]

        # lista com duas cartas iniciais da mesa (pc)
        pc_cartas = [random.choice(cartas), random.choice(cartas)]

        # verifica se a mesa fez blackjack, caso positivo vitória da mesa, neste ponto, empate é vitória da mesa
        if fazer_blackjack(pc_cartas):
            exibir_maos("A mesa fez um Blackjack. Você perdeu!!")
            continue
        # se a mesa não fez blackjack, mas o usuário fez blackjack, vitória do usuário
        elif fazer_blackjack(suas_cartas):
            exibir_maos("Você fez um Blackjack. Você ganhou!!")
            continue
        # se ninguém fez um blackjack na rodada inicial
        else:
            while True:
                # verifica se o usuário tem um 11 e se a pontuação é maior que 21, caso positivo troca o 11 por 1
                if 11 in suas_cartas:
                    if sum(suas_cartas) > 21:
                        x = suas_cartas.index(11)
                        suas_cartas[x] = 1

               # verifica se a mesa tem um 11 e se a pontuação é maior que 21, caso positivo troca o 11 por 1
                if 11 in pc_cartas:
                    if sum(pc_cartas) > 21:
                        x = pc_cartas.index(11)
                        pc_cartas[x] = 1

                # exibi a rodada de cartas
                print(
                    f"Suas cartas: {suas_cartas}, pontuação atual: {sum(suas_cartas)}")
                print(f"Primeira carta da mesa: {pc_cartas[0]}")

                # verifica se o usuário quer nova carta ou verificar o resultado do jogo (passar a mão)
                op2 = input(
                    "Digite 's' para pegar outra carta, ou 'n' para passar: ").lower()
                if op2 == 's':
                    suas_cartas.append(random.choice(cartas))
                    if fazer_blackjack(suas_cartas):
                        exibir_maos("Você fez um Blackjack. Você ganhou!!")
                        break
                    elif sum(suas_cartas) > 21:
                        exibir_maos("Você passou de 21. Você perdeu!!")
                        break
                elif op2 == 'n':
                    while sum(pc_cartas) < 17:
                        pc_cartas.append(random.choice(cartas))
                        # verifica se a mesa fez blackjack, caso positivo vitória da mesa, neste ponto, empate é vitória da mesa
                        if fazer_blackjack(pc_cartas):
                            exibir_maos(
                                "A mesa fez um Blackjack. Você perdeu!!")
                            break
                    # verifica se empate
                    if sum(pc_cartas) > 21:
                        exibir_maos("A mesa passou de 21. Você ganhou!!")
                        break
                    elif sum(suas_cartas) == sum(pc_cartas):
                        exibir_maos("Empate!!")
                        break
                    # verifica se usuário ganhou
                    elif sum(suas_cartas) > sum(pc_cartas):
                        exibir_maos("Você ganhou!!")
                        break
                    # se a mesa(pc) ganhou
                    else:
                        exibir_maos("Você perdeu!!")
                        break

    elif op1 == 'n':
        print("Até a próxima!")
        quero_jogar = False
    else:
        print("Opção inválida")
