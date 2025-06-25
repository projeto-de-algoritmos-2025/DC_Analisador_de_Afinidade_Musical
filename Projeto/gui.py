# interface

import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from data import GENEROS_MUSICAIS, GOSTOS_FAMOSOS
from comparador import comparar

class AppMusical:
    def __init__(self, root):
        self.root = root
        self.root.title("Afinidade Musical 🎵")
        self.ranking = []

        titulo_fonte = tkFont.Font(family="Helvetica", size=18, weight="bold")
        self.label = tk.Label(
            root,
            text="Monte seu ranking musical favorito 🎤✨",
            font=titulo_fonte,
            justify="center"
        )
        self.label.pack(pady=10)

        self.lista = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, font=("Helvetica", 12))
        for genero in GENEROS_MUSICAIS:
            self.lista.insert(tk.END, genero)
        self.lista.pack()

        self.btn_up = tk.Button(root, text="↑ Mover para cima", command=self.mover_para_cima)
        self.btn_up.pack(pady=5)

        self.btn_down = tk.Button(root, text="↓ Mover para baixo", command=self.mover_para_baixo)
        self.btn_down.pack()

        self.btn_finalizar = tk.Button(root, text="Ver Afinidade", command=self.ver_resultado)
        self.btn_finalizar.pack(pady=10)

        self.resultado = tk.Text(root, height=10, width=50)
        self.resultado.pack(pady=5)

    def mover_para_cima(self):
        i = self.lista.curselection()
        if i and i[0] > 0:
            idx = i[0]
            texto = self.lista.get(idx)
            self.lista.delete(idx)
            self.lista.insert(idx - 1, texto)
            self.lista.select_set(idx - 1)

    def mover_para_baixo(self):
        i = self.lista.curselection()
        if i and i[0] < self.lista.size() - 1:
            idx = i[0]
            texto = self.lista.get(idx)
            self.lista.delete(idx)
            self.lista.insert(idx + 1, texto)
            self.lista.select_set(idx + 1)

    def ver_resultado(self):
        ranking_usuario = self.lista.get(0, tk.END)
        resultados = comparar(list(ranking_usuario), GOSTOS_FAMOSOS)

        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(tk.END, "🎧 Famosos com gosto mais parecido:\n\n")
        for i, r in enumerate(resultados):
            self.resultado.insert(tk.END, f"{i+1}º {r['nome']} (diferença: {r['inversoes']})\n")

def iniciar_interface():
    root = tk.Tk()
    app = AppMusical(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_interface()