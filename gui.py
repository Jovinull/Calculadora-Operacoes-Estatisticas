import tkinter as tk
from tkinter import messagebox
from func.media import calcular_media
from func.mediana import calcular_mediana
from func.desvioPadrao import calcular_desvio_padrao

def calcular_estatisticas():
    try:
        numeros = [float(num) for num in entrada.get().split()]
        media = calcular_media(numeros)
        mediana = calcular_mediana(numeros)
        desvio_padrao = calcular_desvio_padrao(numeros)
        resultado.set(f"Média: {media}\nMediana: {mediana}\nDesvio Padrão: {desvio_padrao}")
    except ValueError:
        messagebox.showerror("Erro de entrada", "Por favor, insira apenas números separados por espaços.")

# Janela principal
root = tk.Tk()
root.title("Calculadora de Operações Estatísticas")

# Entrada de números
tk.Label(root, text="Digite os números separados por espaço:").pack()
entrada = tk.Entry(root, width=50)
entrada.pack()

# Botão para calcular
tk.Button(root, text="Calcular", command=calcular_estatisticas).pack()

# Resultado
resultado = tk.StringVar()
tk.Label(root, textvariable=resultado).pack()

root.mainloop()
