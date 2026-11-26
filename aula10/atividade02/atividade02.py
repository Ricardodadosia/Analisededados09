def somar(a, b): 
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None
    return a / b

numero1 = float(input("Introduza o primeiro número: "))
numero2 = float(input("Introduza o segundo número: "))

print("\nEscolha uma operação:")
print("""
[1] soma 
[2] subtrair
[3] multiplicar
[4] dividir 
""")

opcao = input("Opção (1/2/3/4): ").strip()

match opcao:
    case 1:
        resultado = somar(valor)

    case 2:
        resultado = subtrair(valor)

    case 3:
        resultado = multiplicar(valor)

    case 4:
        resultado = dividir(valor)

    case _:
        print('opção invalida')

print(f'resultado: {resultado}')        


