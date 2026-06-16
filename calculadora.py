# ============================================
# calculadora python - atividade
# autor: claudio santos
# ============================================

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "erro: divisao por zero nao e permitida!"
    return round(a / b, 2)

def calculadora():
    print("calculadora python")
    print("")

    try:
        num1 = float(input("digite o primeiro numero: "))
        num2 = float(input("digite o segundo numero: "))
    except ValueError:
        print("erro: digite apenas numeros validos!")
        return

    print("")
    print("escolha a operacao:")
    print("  1 - adicao       (+)")
    print("  2 - subtracao    (-)")
    print("  3 - multiplicacao (x)")
    print("  4 - divisao      (/)")

    opcao = input("digite a opcao (1-4): ")

    print("")

    if opcao == "1":
        resultado = adicao(num1, num2)
        print(f"resultado: {num1} + {num2} = {resultado}")
    elif opcao == "2":
        resultado = subtracao(num1, num2)
        print(f"resultado: {num1} - {num2} = {resultado}")
    elif opcao == "3":
        resultado = multiplicacao(num1, num2)
        print(f"resultado: {num1} x {num2} = {resultado}")
    elif opcao == "4":
        resultado = divisao(num1, num2)
        print(f"resultado: {num1} / {num2} = {resultado}")
    else:
        print("opcao invalida! digite um numero entre 1 e 4.")

    print("")
    print("obrigado por usar a calculadora!")

calculadora()
