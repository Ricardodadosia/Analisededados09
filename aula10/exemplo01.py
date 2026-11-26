def calcula_bonus(v, s):
    b = v * 0.10
    s = s + b
    return b, s

# Inicio do codigo
META = 12000 

venda = float(input('informe o venda do vendendor: '))
salario = float(input('informe o salario: '))



if venda >= META:
    # chama a função p/ bônus de 10%
    bonus, novo_salario = calcula_bonus(venda, salario)
    print(f'\nValor do bonus R$ {bonus}')
    print(f'Salario com bonus R$ {salario}')

else:
    print('Sem Bonus')
    print(f'Salario: R$ {salario}')    