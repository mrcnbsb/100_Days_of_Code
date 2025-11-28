import os

from art import logo
from dados import MENU, recursos, caixa

def limpar_tela():
    os.system('cls')

def verificar_ingredientes(opcao_drink_usuario):
    """Recebe a escolha do usuário e retorna verdadeiro se os ingredientes são suficientes ou falso caso insuficientes."""
    agua_restante = recursos["agua"]
    leite_restante = recursos["leite"]
    cafe_restante = recursos["cafe"]
    if opcao_drink_usuario == "espresso":
        agua_necessaria = MENU["espresso"]["ingredientes"]["agua"]
        leite_necessario = 0
        cafe_necessario = MENU["espresso"]["ingredientes"]["cafe"]
        #return agua_restante >= agua_necessaria and leite_restante >= leite_necessario and cafe_restante >= cafe_necessario
        if agua_restante >= agua_necessaria:
            if leite_restante >= leite_necessario:
                if cafe_restante >= cafe_necessario:
                    return True
                else:
                    return "cafe"
            else:
                return "leite"
        else:
            return "agua"
    elif opcao_drink_usuario == "latte":
        agua_necessaria = MENU["latte"]["ingredientes"]["agua"]
        leite_necessario = MENU["latte"]["ingredientes"]["leite"]
        cafe_necessario = MENU["latte"]["ingredientes"]["cafe"]
        #return agua_restante >= agua_necessaria and leite_restante >= leite_necessario and cafe_restante >= cafe_necessario
        if agua_restante >= agua_necessaria:
            if leite_restante >= leite_necessario:
                if cafe_restante >= cafe_necessario:
                    return True
                else:
                    return "cafe"
            else:
                return "leite"
        else:
            return "agua"
    else:
        agua_necessaria = MENU["cappuccino"]["ingredientes"]["agua"]
        leite_necessario = MENU["cappuccino"]["ingredientes"]["leite"]
        cafe_necessario = MENU["cappuccino"]["ingredientes"]["cafe"]
        #return agua_restante >= agua_necessaria and leite_restante >= leite_necessario and cafe_restante >= cafe_necessario
        if agua_restante >= agua_necessaria:
            if leite_restante >= leite_necessario:
                if cafe_restante >= cafe_necessario:
                    return True
                else:
                    return "cafe"
            else:
                return "leite"
        else:
            return "agua"

def calcular_caixa():
    """Retorna o valor total de dinheiro no caixa."""
    quartes = caixa["quartes"] * 0.25
    dimes =  caixa["dimes"] * 0.10
    nickles = caixa["nickles"] * 0.05
    pennies = caixa["pennies"] * 0.01
    return quartes + dimes + nickles + pennies

def gerar_relatorio():
    agua = recursos["agua"]
    leite = recursos["leite"]
    cafe = recursos["cafe"]
    caixa = calcular_caixa()
    print(f"\nÁgua: {agua}ml\nLeite: {leite}ml\nCafé: {cafe}g\nCaixa: R$ {caixa}")

def fazer_cafe(opcao_drink_usuario):
    """Recebe a opção de drink do usuário, decrementa os ingredientes, gera relatório antes e depois e informa que o drink está servido."""
    if opcao_drink_usuario == "espresso":
        agua_necessaria = MENU["espresso"]["ingredientes"]["agua"]
        leite_necessario = 0
        cafe_necessario = MENU["espresso"]["ingredientes"]["cafe"]
    elif opcao_drink_usuario == "latte":
        agua_necessaria = MENU["latte"]["ingredientes"]["agua"]
        leite_necessario = MENU["latte"]["ingredientes"]["leite"]
        cafe_necessario = MENU["latte"]["ingredientes"]["cafe"]
    else:
        agua_necessaria = MENU["cappuccino"]["ingredientes"]["agua"]
        leite_necessario = MENU["cappuccino"]["ingredientes"]["leite"]
        cafe_necessario = MENU["cappuccino"]["ingredientes"]["cafe"]
    recursos["agua"] -= agua_necessaria
    recursos["leite"] -= leite_necessario
    recursos["cafe"] -= cafe_necessario
    print(f"\nAqui está o seu {opcao_drink_usuario}. Aproveite!")

def depositar_moedas():
    """Retorna o valor total inserido pelo usuário em moedas"""
    moedas_recebidas = {
        "q": 0,
        "d": 0,
        "n": 0,
        "p": 0,
    }
    numero = 1
    moeda_usuario = -1
    while moeda_usuario != "0":
        moeda_usuario = input(f"""Coloque a {numero} moeda.        
        Digite 'q' para quarters ($0.25)
        Digite 'd' para dimes ($0.10)
        Digite 'n' para nickles ($0.05)
        Digite 'p' para pennies ($0.01)
        Digite 0 para sair: """).lower()
        numero += 1
        for moeda in moedas_recebidas:
            if moeda == moeda_usuario:
                moedas_recebidas[moeda] += 1
        total = 0
    return moedas_recebidas

def calcular_valor_depositado(moedas_recebidas):
    """Recebe um dicionário com a quantidade de moedas de cada valor, realiza o cálculo e retorna o total"""
    total_q = moedas_recebidas["q"] * 0.25
    total_d = moedas_recebidas["d"] * 0.1
    total_n = moedas_recebidas["n"] * 0.05
    total_p = moedas_recebidas["p"] * 0.01
    total_depositado = total_q + total_d + total_n + total_p
    return total_depositado

def lancar_caixa(moedas_recebidas):
    caixa["quartes"] += moedas_recebidas["q"]
    caixa["dimes"] += moedas_recebidas["d"]
    caixa["nickles"] += moedas_recebidas["n"]
    caixa["pennies"] += moedas_recebidas["p"]
    print("Caixa atualizado com sucesso!")

def calcular_troco(opcao_drink_usuario, valor_depositado):
    """Recebe a opção de drink do usuário e o total depositado em moedas e retorna a diferença"""
    troco = valor_depositado - MENU[opcao_drink_usuario]["custo"]
    return troco

def retornar_troco(troco):
    q = troco // 0.25
    if caixa["quartes"] >= q:
        troco = round(troco % 0.25, 2)
        caixa["quartes"] -= q
    else:
        q = 0

    d = troco // 0.10
    if caixa["dimes"] >= d:
        troco = round(troco % 0.10, 2)
        caixa["dimes"] -= d
    else:
        d = 0

    n = troco // 0.05
    if caixa["nickles"] >= n:
        troco = round(troco % 0.05, 2)
        caixa["nickles"] -= n
    else:
        n = 0

    p = troco // 0.01
    if caixa["pennies"] >= p:
        caixa["pennies"] -= p
    else:
        p = 0

    total = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    if total != 0.0:
        print(f"Troco de {int(q)} quartes, {int(d)} dimes, {int(n)} nickles e {int(p)} pennies, total de $ {total}.")

def abastecer_caixa_para_troco():
    q = int(input("Informe a quantidade de moedas de 'quartes': "))
    d = int(input("Informe a quantidade de moedas de 'dimes': "))
    n = int(input("Informe a quantidade de moedas de 'nickle's: "))
    p = int(input("Informe a quantidade de moedas de 'pennies': "))
    caixa["quartes"] = q
    caixa["dimes"] = d
    caixa["nickles"] = n
    caixa["pennies"] = p

def exibir_valor_produto(opcao_usuario):
    for opcao in MENU:
        if opcao == opcao_usuario:
            print(f"\nCafé {opcao}: $ {MENU[opcao]['custo']}")

def abastecer_ingredientes():
    recursos["agua"] = 300
    recursos["leite"] = 200
    recursos["cafe"] = 100
    print("Máquina abastecida com sucesso!")

# maquina ligada
is_on = True

limpar_tela()
print(logo)

# depositar moedas no caixa para que o troco seja possível
abastecer_caixa_para_troco()
limpar_tela()

# enquanto máquina ligada
while is_on:
    # opcao do usuario
    choice = input("O que você gostaria? (espresso/latte/cappuccino): ")

    # se opcao == off, is_on = False, fim do loop (maquina desligada)
    if choice == 'off':
        is_on = False

    # se choice == report, gera um relatório que exibe o total restante de ingredientes e valor em caixa
    if choice == 'report':
        gerar_relatorio()

    # se choice == espresso ou latte ou cappuccino, entra no if
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":

        # verifica se há ingredientes para a escolha do usuário
        resposta = verificar_ingredientes(choice)

        # se resposta == agua ou leite ou cafe, significa que falta este ingrediente
        # se faltar o ingrediente, exibe mensagem de erro e retorna ao início do loop finalizando o pedido
        if resposta == "agua" or resposta == "leite" or resposta == "cafe":
            print(f"Sinto muito, não há {resposta} suficiente.")
            continue

        # caso haja ingredientes o fluxo continua

        # retorna as moedas depositadas pelo usuario
        moedas_recebidas = depositar_moedas()

        # com base nas moedas depositadas, retorna o valor total depositado
        valor_depositado = calcular_valor_depositado(moedas_recebidas)

        # se o valor depositado for insuficiente, exibe mensagem de erro e retorna ao início do loop finalizando o pedido
        if valor_depositado < MENU[choice]["custo"]:
            print("Sinto muito, o dinheiro não é suficiente. Dinheiro devolvido!")
            continue

        # caso o valor depositado seja suficiente

        # lanca as moedas no caixa
        lancar_caixa(moedas_recebidas)

        # verifica se há troco (valor depositado > custo)
        troco = calcular_troco(choice, valor_depositado)

        # retorna troco caso haja
        retornar_troco(troco)

        # preparar o café
        fazer_cafe(choice)
