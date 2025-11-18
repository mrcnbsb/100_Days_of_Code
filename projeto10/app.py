def add(n1, n2):
    """Função para adição que recebe dois números como parâmetros e retorna o resultado do primeiro adicionado do segundo."""
    return n1 + n2

def subtract(n1, n2):
    """Função para subtração que recebe dois números como parâmetros e retorna o resultado do primeiro subtraído do segundo."""
    return n1 - n2

def multiply(n1, n2):
    """Função para multiplicação que recebe dois números como parâmetros e retorna o resultado do primeiro multiplicado pelo segundo."""
    return n1 * n2

def divide(n1, n2):
    """Função para divisão que recebe dois números como parâmetros e retorna o resultado do primeiro dividido pelo segundo."""
    return n1 / n2

from art import logo


operacacoes = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculadora():
    print(logo)

    # variável para controle do loop
    devo_acumular = True

    # captura do primeiro número com input e casting para float
    num1 = float(input("Qual é o primeiro número?: "))

    while devo_acumular:

        for simbolo in operacacoes:
            print(simbolo)
        simbolo_operacao = input("Escolha uma operação: ")

        num2 = float(input("Qual é o segundo número?: "))

        resultado = operacacoes[simbolo_operacao](num1, num2)
        print(f"{num1} {simbolo_operacao} {num2} = {resultado}")

        opcao = input(f"Digite 's' para continuar com o {resultado} ou 'n' para nova operação: ").lower()
        if opcao == "s":
            num1 = resultado
        else:
            devo_acumular = False
            print("\n" * 20)
            calculadora()

calculadora()
