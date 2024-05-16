def Counter(numeros):
    contador = {}
    for numero in numeros:
        if numero in contador:
            contador[numero] += 1
        else:
            contador[numero] = 1
    return contador
