print("Bem-vindo à Calculadora de Gorjetas!")
conta = float(input("Qual o total da conta? R$"))
gorjeta = int(input("Qual o percentua de gorjeta você gostaria de dar? 10 12 15 "))
pessoas = int(input("Quantas pessoas irão dividir a conta? "))
pagamento = conta * (1 + gorjeta / 100) / pessoas
print(f"Cada pessoa deverá pagar: ${round(pagamento, 2)}")
            