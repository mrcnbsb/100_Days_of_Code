import random
from forca_arte import estagios, logo
from forca_palavras import palavras

print(logo)

# escolhe uma palavra da lista de palavras de modo aleatório
palavra_escolhida = random.choice(palavras)

# exibe pro usuário quantas letras a palavra a ser advinhada tem
espacos = ""
for letra in palavra_escolhida:
    espacos += "_"
print("Palavra pra advinhar: " + espacos)

# variáveis para controle de vidas, loop e formação do display
vidas = 6
fim_jogo = False
letrasAcertadas = []

while not fim_jogo:

    # exibe número de vidas restantes e captura a letra escolhida pelo usuário
    print(f"--- Você ainda tem {vidas}/6 chances! ---")
    escolhaUsuario = input("Que letra você escolhe? ").lower()

    # mensagem se a letra escolhida já tiver sido advinhada
    if escolhaUsuario in letrasAcertadas:
        print(f"Você já adivinhou a letra '{escolhaUsuario}'")

    display = ""

    # verifica se a letra escolhida está na palavra
    # caso esteja a exibe no display
    # caso não esteja exibe "_"
    # caso tenha sido advinhada antes a exibe
    for letra in palavra_escolhida:
        if letra == escolhaUsuario:
            display += escolhaUsuario
            letrasAcertadas.append(escolhaUsuario)
        elif letra in letrasAcertadas:
            display += letra
        else:
            display += "_"

    # exibe o display ao final de cada interação
    print("Palavra pra advinhar: " + display)

    # se a escolha do usuário não estiver na palavra perde uma vida
    if escolhaUsuario not in palavra_escolhida:
        vidas -= 1
        print(
            f"Você escolheu '{escolhaUsuario}', que não está na palavra. Você perdeu uma vida.")
        # se perder todas as vidas o jogo acaba
        if vidas == 0:
            fim_jogo = True
            print("Você perdeu!")
            print(f"A palavra era: {palavra_escolhida}")

    # se preencher o display com letras vence o jogo
    print(display)
    if "_" not in display:
        fim_jogo = True
        print("Você venceu!")

    # arte para mostrar o estágio da forca
    print(estagios[vidas])
