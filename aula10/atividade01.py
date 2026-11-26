LIMITE_PESO = 100.0
VALOR_MULTA_POR_KG = 4.0


def calcular_multa(peso_total):
    multa = 0.0
    if peso_total > LIMITE_PESO:
        excesso = peso_total - LIMITE_PESO
        multa = excesso * VALOR_MULTA_POR_KG
    return multa


def main():
    peso = float(input("Informe o peso total de peixes pescados no dia (em kg): "))
    multa = calcular_multa(peso)

    mensagem = f"Peso dentro do limite de {LIMITE_PESO:.0f} kg. Não há multa."
    if multa > 0:
        excesso = peso - LIMITE_PESO
        mensagem = (
            f"Limite de {LIMITE_PESO:.0f} kg ultrapassado em {excesso:.2f} kg. "
            f"Valor da multa: R$ {multa:.2f}"
        )

    print(mensagem)

if __name__ == "__main__":
    main()



