LIMITE_PESO = 100.0
VALOR_MULTA_POR_KG = 4.0


def obter_peso_pescado():
    return float(input("Informe o peso total de peixes pescados no dia (em kg): "))


def calcular_excesso(peso_total):
    if peso_total > LIMITE_PESO:
        return peso_total - LIMITE_PESO
    return 0.0


def calcular_multa(excesso):
    return excesso * VALOR_MULTA_POR_KG


def exibir_resultado(peso_total, excesso, multa):
    if excesso > 0:
        print(
            f"Peso informado: {peso_total:.2f} kg | Excesso: {excesso:.2f} kg | "
            f"Valor da multa: R$ {multa:.2f}"
        )
    else:
        print(
            f"Peso informado: {peso_total:.2f} kg | "
            f"Dentro do limite de {LIMITE_PESO:.0f} kg. Não há multa."
        )


def main():
    peso = obter_peso_pescado()
    excesso = calcular_excesso(peso)
    multa = calcular_multa(excesso)
    exibir_resultado(peso, excesso, multa)


if __name__ == "__main__":
    main()