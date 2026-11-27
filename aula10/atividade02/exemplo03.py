import subprocess
import random


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


# Início
os.system("cls" if os.name == "nt" else "clear")

num1 = random.randint(10, 100)
num2 = random.randint(1, 10)
print(f"Número 1: {num1} e Número 2: {num2}")

print("\nEscolha uma operação:")
print("""
[1] soma
[2] subtrair
[3] multiplicar
[4] dividir
""")

opcao = input("Opção (1/2/3/4): ").strip()
resultado = None

match opcao:
    case "1":
        resultado = somar(num1, num2)
    case "2":
        resultado = subtrair(num1, num2)
    case "3":
        resultado = multiplicar(num1, num2)
    case "4":
        resultado = dividir(num1, num2)
        if resultado is None:
            print("Erro: divisão por zero não é permitida.")
    case _:
        print("Opção inválida.")

if resultado is not None:
    print(f"Resultado: {resultado:.2f}" if opcao == "4" else f"Resultado: {resultado}")