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


# def calcular_quartil_01(conjunto, debug=True):
#     """
#     Implementação do cálculo de quartil

#     no octave: quantile(conjunto, [0.25, 0.5, 0.75])
#     """
#     tamanho = len(conjunto)
#     conjunto_ordenado = sorted(conjunto)
#     posicao_q1 = math.ceil((tamanho + 1) * (1 / 4)) - 1
#     if debug:
#         print((tamanho + 1) * (1 / 4))

#     posicao_q1_menor = conjunto_ordenado[posicao_q1 - 1]
#     posicao_q1_maior = conjunto_ordenado[posicao_q1]
#     if debug:
#         print("(0.25 * {}) + (0.75 * {})".format(posicao_q1_menor, posicao_q1_maior))

#     # média ponderada
#     q1 = (0.25 * posicao_q1_menor) + (0.75 * posicao_q1_maior)
#     q2 = calcular_mediana(conjunto_ordenado)

#     posicao_q3 = math.ceil((tamanho + 1) * (3 / 4)) - 1
#     if debug:
#         print((tamanho + 1) * (3 / 4))

#     posicao_q3_menor = conjunto_ordenado[posicao_q3 - 1]
#     posicao_q3_maior = conjunto_ordenado[posicao_q3]
#     if debug:
#         print("(0.75 * {}) + (0.25 * {})".format(posicao_q3_menor, posicao_q3_maior))

#     # média ponderada
#     q3 = (0.75 * posicao_q3_menor) + (0.25 * posicao_q3_maior)
#     return q1, q2, q3


# def calcular_quartil_02(conjunto, debug=True):
#     """
#     Implementação do cálculo de quartil

#     no octave: quantile(conjunto, [0.25, 0.5, 0.75])
#     """
#     tamanho = len(conjunto)
#     conjunto_ordenado = sorted(conjunto)

#     posicao_q1 = math.ceil(tamanho * (1 / 4)) - 1
#     q1 = conjunto_ordenado[posicao_q1]

#     q2 = calcular_mediana(conjunto_ordenado)

#     posicao_q3 = math.ceil(tamanho * (3 / 4)) - 1
#     q3 = conjunto_ordenado[posicao_q3]
#     return q1, q2, q3


def calcular_quartil(conjunto, debug=True):
    """
    Implementação do cálculo de quartil

    no octave: quantile(conjunto, [0.25, 0.5, 0.75])
    """
    tamanho = len(conjunto)
    conjunto_ordenado = sorted(conjunto)
    posicao_q1 = math.ceil((tamanho + 1) * (1 / 4)) - 1
    if debug:
        print((tamanho + 1) * (1 / 4))

    posicao_q1_menor = conjunto_ordenado[posicao_q1 - 1]
    posicao_q1_maior = conjunto_ordenado[posicao_q1]
    if debug:
        print("({} + {}) / 2.0".format(posicao_q1_menor, posicao_q1_maior))

    # média comum
    q1 = (posicao_q1_menor + posicao_q1_maior) / 2.0
    q2 = calcular_mediana(conjunto_ordenado)

    posicao_q3 = math.ceil((tamanho + 1) * (3 / 4)) - 1
    if debug:
        print((tamanho + 1) * (3 / 4))

    posicao_q3_menor = conjunto_ordenado[posicao_q3 - 1]
    posicao_q3_maior = conjunto_ordenado[posicao_q3]
    if debug:
        print("({} + {}) / 2.0".format(posicao_q3_menor, posicao_q3_maior))

    # média comum
    q3 = (posicao_q3_menor + posicao_q3_maior) / 2.0
    return q1, q2, q3
