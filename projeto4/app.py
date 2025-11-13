import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
figuras = [pedra, papel, tesoura]
# escolha do usuário com input
usuarioEscolha = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
if usuarioEscolha == 0:
    print(figuras[usuarioEscolha])
elif usuarioEscolha == 1:
    print(figuras[usuarioEscolha])
elif usuarioEscolha == 2:
    print(figuras[usuarioEscolha])
else:
    pass

# Escolha do PC com a biblioteca random
PCEscolha = random.randint(0, 2)
print("Computador escolhe:")
if PCEscolha == 0:
    print(figuras[PCEscolha])
elif PCEscolha == 1:
    print(figuras[PCEscolha])
else:
    print(figuras[PCEscolha])

# Quem venceu?
if usuarioEscolha == PCEscolha:
    print("Empate!")
elif usuarioEscolha == 0 and PCEscolha == 1:
    print("Você perdeu!")
elif usuarioEscolha == 0 and PCEscolha == 2:
    print("você ganhou!")
elif usuarioEscolha == 1 and PCEscolha == 0:
    print("você ganhou!")
elif usuarioEscolha == 1 and PCEscolha == 2:
    print("Você perdeu!")
elif usuarioEscolha == 2 and PCEscolha == 0:
    print("Você perdeu!")
elif usuarioEscolha == 2 and PCEscolha == 1:
    print("você ganhou!")
else:
    print("Você digitou um número inválido. Você perdeu!")