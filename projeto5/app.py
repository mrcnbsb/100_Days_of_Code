import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao Gerador de Password!")
nr_letras = int(input("Quantas letras você gostaria no seu password?\n"))
nr_simbolos = int(input(f"Quantos símbolos você gostaria?\n"))
nr_numeros = int(input(f"Quantos números você gostaria?\n"))

password = ""
for letra in range(nr_letras):
    password += random.choice(letras)

for simbolo in range(nr_simbolos):
    password += random.choice(simbolos)

for numero in range(nr_numeros):
    password += random.choice(numeros)

# converto a string em lista
password = list(password)

# shuffle pra bagunçar a lista
random.shuffle(password)

# join pra juntar os elementos da lista e formar uma string
password = "".join(password)

print(f"O seu password é {password}")