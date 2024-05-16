from utils.counter import Counter

def calcular_moda(numeros):
    contador = Counter(numeros)
    moda = []
    
    # Itera sobre cada par chave-valor no dicionário contador
    for k, v in contador.items():
        # Verifica se o valor (v) é igual ao valor máximo de contagem no contador
        if v == max(contador.values()):
            # Se sim, adiciona a chave (k) à lista moda
            moda.append(k)
    
    return moda
