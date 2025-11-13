print("\n*** Bem-vindo à Ilha do Tesouro Heróico ***")
print("""Você acorda em uma ilha misteriosa. Dizem que há um tesouro escondido que dá
poderes infinitos... mas cuidado! Vilões também estão atrás dele!
Você está pronto(a)? Vamos nessa!""")

print("\nVocê está na praia. Dois caminhos surgem: um pela floresta sombria e outro pelas ruínas antigas.")
decisao = input("Qual você escolhe? ('floresta' ou 'ruinas') ").lower()
if decisao == 'floresta':
    print("Corajoso! A floresta tem mistérios, mas você avança com determinação!")

    print("\nVocê chega a um rio. Pode tentar atravessar nadando ou construir uma ponte com galhos")
    decisao = input("O que faz? ('nadar' ou 'ponte') ").lower()
    if decisao == "ponte":
        print("Boa escolha! Você constrói uma ponte firme e passa ileso.")

        print("\nVocê encontra uma caverna com fogo saindo da entrada")
        decisao = input("Pode entrar com cuidado ou dar a volta pela montanha. ('entrar' ou 'voltar') ").lower()
        if decisao == "entrar":
            print("Você encara o calor e encontra uma tocha mágica!")

            print("\nVocê chega ao topo da ilha e vê o baú do tesouro. Mas um vilão o guarda: Loki!")
            decisao = input("Você tenta enganá-lo com uma ilusão ou enfrentá-lo com sabedoria? ('ilusão' ou 'sabedoria') ").lower()
            if decisao == "sabedoria":
                print("Você recita o Código dos Heróis e confunde Loki com sua própria lógica!")
                print("Inteligência vence força quando o coração é justo.")
                print("\nVocê abre o baú e encontra o TESOURO DOS HERÓIS!")
                print("Parabéns. A verdadeira vitória é nunca desistir — e rir até dos próprios erros!")
                print("\nVocê venceu!")

            else:
                print("Você tenta enganar o mestre das ilusões… e ele te aplaude antes de transformar você num sapo falante!")
                print('Loki: “Belo esforço, anfíbio!”')
                print("\nFim de jogo!")
        else:
            print("Ao dar a volta, você esbarra no Coringa montado em um unicórnio explosivo!")
            print('Coringa: "Sério que achou que fugir era uma boa piada?"')
            print("\nFim de jogo!")
    else:
        print("Você pula na água… e o Tubarão-Rei aparece com um sorriso faminto!")
        print('Tubarão-Rei: "Amigo... ou almoço?"')
        print("\nFim de jogo!")
else:
    print("Você entrou nas ruínas… e foi recebido por Thanos fazendo ioga!")
    print('Thanos: “Equilíbrio é tudo, inclusive o seu fim!”')
    print("\nFim de jogo!")