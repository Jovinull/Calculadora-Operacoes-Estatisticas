import tkinter as tk
from tkinter import messagebox
from func.media import calcular_media
from func.mediana import calcular_mediana
from func.desvioPadrao import calcular_desvio_padrao

def calcular_estatisticas():
    try:
        entrada_texto = entrada.get()
        numeros_texto = entrada_texto.split()
        numeros = []
        for num in numeros_texto:
            numeros.append(float(num))

        media = calcular_media(numeros)
        mediana = calcular_mediana(numeros)
        desvio_padrao = calcular_desvio_padrao(numeros)
        resultado.set(f"Média: {media}\nMediana: {mediana}\nDesvio Padrão: {desvio_padrao}")
    except ValueError:
        messagebox.showerror("Erro de entrada", "Por favor, insira apenas números separados por espaços.")

root = tk.Tk()
root.title("Calculadora de Operações Estatísticas")

tk.Label(root, text="Digite os números separados por espaço:").pack()
entrada = tk.Entry(root, width=50)
entrada.pack()

tk.Button(root, text="Calcular", command=calcular_estatisticas).pack()

resultado = tk.StringVar()
tk.Label(root, textvariable=resultado).pack()

root.mainloop()
