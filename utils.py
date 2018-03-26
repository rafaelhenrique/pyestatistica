import math


def calcular_media(conjunto):
    return sum(conjunto) / len(conjunto)


def calcular_mediana(conjunto):
    conjunto_ordenado = sorted(conjunto)
    # localizar mediana de conjunto par
    if len(conjunto_ordenado) % 2 == 0:
        meio = int(len(conjunto_ordenado) / 2) - 1
        return (conjunto_ordenado[meio] + conjunto_ordenado[meio + 1]) / 2

    # localizar mediana de conjunto ímpar
    else:
        meio = int((len(conjunto_ordenado) / 2) - 0.5)
        return conjunto_ordenado[meio]


def calcular_variancia_amostral(conjunto):
    media = calcular_media(conjunto)
    novo_conjunto = [elemento - media for elemento in conjunto]

    if sum(novo_conjunto) != 0:
        raise Exception("Erro de cálculo")

    conjunto_quadrados = [elemento ** 2 for elemento in novo_conjunto]
    return sum(conjunto_quadrados) / (len(conjunto_quadrados) - 1)


def calcular_desvpad(conjunto):
    """Implementação do desvio padrão"""
    variancia_amostral = calcular_variancia_amostral(conjunto)
    return math.sqrt(variancia_amostral)


def calcular_dma(conjunto):
    """
    Implementação do desvio médio absoluto

    no octave: mean (abs (conjunto - mean (conjunto))
    """
    media = calcular_media(conjunto)
    novo_conjunto = [abs(elemento - media) for elemento in conjunto]
    return calcular_media(novo_conjunto)


def calcular_dmeda(conjunto):
    """
    Implementação do desvio mediano absoluto

    no octave: median (abs (conjunto - mean (conjunto))
    """
    media = calcular_media(conjunto)
    novo_conjunto = [abs(elemento - media) for elemento in conjunto]
    return calcular_mediana(novo_conjunto)


def calcular_percentil(conjunto, p):
    """
    Implementação do cálculo de percentil
    também pode ser usado para cálculo de quartil (0.25, 0.5 e 0.75)

    conjunto é uma lista de elementos
    p deve ser um valor percentual já calculado (0.25, 0.4 etc)
    """
    conjunto_ordenado = sorted(conjunto)

    if p == 0:
        return conjunto_ordenado[0]
    elif p == 1:
        return conjunto_ordenado[-1]

    m = len(conjunto_ordenado)
    k = m * p
    k = k - 1  # ajustando lista python

    if not k.is_integer():
        k = int(math.ceil(k))
        return conjunto_ordenado[k]

    k = int(k)
    return (conjunto_ordenado[k] + conjunto_ordenado[k + 1]) / 2.


def calcular_intervalo(conjunto):
    conjunto_ordenado = sorted(conjunto)
    return conjunto_ordenado[-1] - conjunto_ordenado[0]


def calcular_intervalo_interquartil(conjunto):
    return calcular_percentil(conjunto, p=0.75) - calcular_percentil(conjunto, p=0.25)
