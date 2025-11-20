import random
import os
from art import logo

def dar_carta():
    """Retorna uma carta aleatória do baralho"""
    # Ás = 11 ou 1
    # Valete, Dama e Rei = 10
    # 2 = 2, 3 = 3, ..., 10 = 10
    # lista com as cartas para sorteio com a random.choice
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta = random.choice(cartas)
    return carta

def calcular_pontuacao(cartas):
    """Recebe uma lista de cartas e retorna a soma dos valores ou 0 se a soma igual a 21"""
    # retorna 0 se Blackjack
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0
    # verica se há Ás(11) entre as cartas, se a soma ultrapassar 21 substitui 11 por 1
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system("cls")

def comparar_pontuacao(pont_usuario, pont_pc):
    if pont_usuario == pont_pc:
        return "Empate 🙃"
    elif pont_pc == 0:
        return "Você perdeu, a mesa fez um Blackjack. 😱"
    elif pont_usuario == 0:
        return "Venceu com um Blackjack. 😎"
    elif pont_usuario > 21:
        return "Você passou de 21. Você perdeu. 😭"
    elif pont_pc > 21:
        return "A mesa passou de 21. Você  venceu. 😬"
    elif pont_usuario > pont_pc:
        return "Você venceu. 😁"
    else:
        return "Você perdeu. 😫"

def jogar():
    print(logo)
    # controle do fluxo do jogo, encerra o loop se True
    e_fim_jogo = False

    usuario_cartas = []
    pc_cartas = []

    pontuacao_usuario = -1
    pontuacao_pc = -1

    # add duas cartas à lista do usuario e à lista da mesa
    for _ in range(2):
        usuario_cartas.append(dar_carta())
        pc_cartas.append(dar_carta())

    while not e_fim_jogo:
        # add às pontuações do usuario e do pc o cálculo da soma das cartas
        pontuacao_usuario = calcular_pontuacao(usuario_cartas)
        pontuacao_pc = calcular_pontuacao(pc_cartas)

        # verifica se blackjack ou se usuario passou de 21
        if pontuacao_usuario == 0 or pontuacao_pc == 0 or pontuacao_usuario > 21:
            e_fim_jogo = True
        else:
            # exibi a rodada de cartas
            print(f"\nSuas cartas: {usuario_cartas}, pontuação atual: {pontuacao_usuario}")
            print(f"Primeira carta da mesa: {pc_cartas[0]}")

            # verifica se o usuario quer nova carta ou verificar o resultado do jogo (passar a mão)
            op2 = input("Digite 's' para pegar outra carta, ou 'n' para passar: ").lower()
            if op2 == 's':
                usuario_cartas.append(dar_carta())
            elif op2 == 'n':
                e_fim_jogo = True
            else:
                print("Opção inválida!")

    # add carta enquanto a pontuação do pc for inferior a 17
    while pontuacao_pc < 17 and pontuacao_pc != 0:
        pc_cartas.append(dar_carta())
        pontuacao_pc = calcular_pontuacao(pc_cartas)

    # exibe resultado final do jogo
    print(f"\nSua mão final: {usuario_cartas}, pontuação final: {pontuacao_usuario}")
    print(f"Mão final da mesa: {pc_cartas}, pontuação final: {pontuacao_pc} ")
    print(comparar_pontuacao(pontuacao_usuario, pontuacao_pc))

while input("\nVocê quer jogar Blackjack? Digite 's' ou 'n': ").lower() == 's':
    limpar_tela()
    jogar()

print("Até a próxima!")


