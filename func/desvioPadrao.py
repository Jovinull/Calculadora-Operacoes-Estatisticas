import math
from func.media import calcular_media

def calcular_desvio_padrao(numeros):
    media = calcular_media(numeros)
    somatorio = sum((x - media) ** 2 for x in numeros)
    variancia = somatorio / len(numeros)
    desvio_padrao = math.sqrt(variancia)
    return desvio_padrao
