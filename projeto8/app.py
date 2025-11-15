import art

print(art.logo)

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(texto_original, deslocamento, encode_or_decode):
    texto_saida = ""
    if encode_or_decode == "decode":
        deslocamento *= -1

    for letra in texto_original:

        if letra not in alfabeto:
            texto_saida += letra
        else:
            posicao_deslocamento = alfabeto.index(letra) + deslocamento
            posicao_deslocamento %= len(alfabeto)
            texto_saida += alfabeto[posicao_deslocamento]
    print(f"Aqui está o resultado do {encode_or_decode}: {texto_saida}")


devo_continuar = True

while devo_continuar:

    direcao = input("Digite 'encode' para encriptar, digite 'decode' para decriptar:\n").lower()
    texto = input("Digite sua mensagem:\n").lower()
    deslocamento = int(input("Digite o número de deslocamento:\n"))

    caesar(texto_original=texto, deslocamento=deslocamento, encode_or_decode=direcao)

    recomecar = input("Digite 'sim' se você quer continuar. De outro modo, digite 'nao'.\n").lower()
    if recomecar == "nao":
        devo_continuar = False
        print("Tchau!")


