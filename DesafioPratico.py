def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == "5":
            print("Encerrando a calculadora.")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print(f"Resultado: {somar(num1, num2)}")
        elif opcao == "2":
            print(f"Resultado: {subtrair(num1, num2)}")
        elif opcao == "3":
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcao == "4":
            print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("Opção inválida! Tente novamente.")

calculadora()