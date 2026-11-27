import random
import subprocess
from auxiliar.funcoes import dobro, triplo, quadrado

subprocess.run('cls', shell=True)
valor = random.randint(1, 10)
print(valor)

print("""
[2] dobro 
[3] triplo
[4] quadrado 
""")

opcao = int(input('informe a opcão: '))

match opcao:
    case 2:
        resultado = dobro(valor)

    case 3:
        resultado = triplo(valor)

    case 4:
        resultado = quadrado(valor)

    case _:
        print('opção invalida')

print(f'resultado: {resultado}')        


