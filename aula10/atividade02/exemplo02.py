def dobro(x):
    res = x *2
    return res 

def triplo(x):
    res = x * 3
    return res 


def quadrado(x):
    res = x **2
    return res 

valor = float(input('informe o valor: '))
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


