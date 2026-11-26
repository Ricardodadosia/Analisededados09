def calcula_multa(e):
    m = e * MULTA
    return m 


MULTA = 4 
LIMITE = 200 

peso = float(input('Informe o peso: '))

if peso > LIMITE:
    execedente = peso - LIMITE
    multa = calcula_multa(execedente)

    print(f'o valor da multa e R$ {multa}')

else:
    print('não ha multa')