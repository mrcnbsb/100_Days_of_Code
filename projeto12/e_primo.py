def e_primo(num):
    cont = 2
    for x in range(2, num):
        if num % x == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False
    

print(e_primo(73))
print(e_primo(75))
print(e_primo(7))
print(e_primo(2))