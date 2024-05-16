def max_valor(dicionario):
    maximo = 0

    for valor in dicionario.values():
        if valor > maximo:
            maximo = valor

    return maximo
