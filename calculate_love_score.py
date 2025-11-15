def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()        
    total1 = 0
    total2 = 0
    for letter in name1:
        if letter in "true":
            total1 += 1            
        if letter in "love":
            total2 += 1            
    for letter in name2:
        if letter in "true":
            total1 += 1            
        if letter in "love":
            total2 += 1
    return (str(total1)+str(total2))           
    

name1 = input("\nInforme o primeiro nome: ")
name2 = input("Informe o segundo nome: ")
print(f"\nO score desse amor é {calculate_love_score(name1, name2)}. Wow!")
