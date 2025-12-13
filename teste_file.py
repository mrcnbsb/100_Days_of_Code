with open("arquivo.txt", "w", encoding="utf-8") as arq:
    arq.write("quero;isso;no;arquivo\n")
  

with open("arquivo.txt", "r") as arq:
    palavras = arq.read().split(";")
    for palavra in palavras:
        print(palavra)


