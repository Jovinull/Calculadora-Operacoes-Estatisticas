def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    meio = n // 2

    if n % 2 == 0:  # se for par
        mediana = (numeros_ordenados[meio - 1] + numeros_ordenados[meio]) / 2
    else:  # se for ímpar
        mediana = numeros_ordenados[meio]

    return mediana
