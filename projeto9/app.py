from art import logo

def encontrar_maior_lance(dicionario_de_lances):
    vencedor = ""
    maior_lance = 0
    for licitante in dicionario_de_lances:
        valor_lance = dicionario_de_lances[licitante]
        if valor_lance > maior_lance:
            maior_lance = valor_lance
            vencedor = licitante
    print(f"O vencedor é {vencedor} com um lance de R$ {maior_lance:.2f}.")
    



print(logo)

# controle do loop
leilao = True

# dicionário que armazena os lances {nome: lance}
lances = {}

while leilao:
    # captura o nome do licitante
    nome = input("Qual o seu nome?: ")
    # captura o valor do lance
    lance = float(input("Qual o seu lance?: R$"))
    # armazena o nome e o valor do lance no dicionario como par {nome: lance}
    lances[nome] = lance
    # verifica se há novos lances ou se deve encontrar o vencedor
    devo_continuar = input("Haverá outros lances? Digite 'sim' ou 'nao': \n").lower()
    if devo_continuar == "nao":
        leilao = False
        encontrar_maior_lance(lances)
    elif devo_continuar == "sim":
        print("\n" * 100)
    
    



