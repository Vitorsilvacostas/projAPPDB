import tkinter as tk
from tkinter import *

class SistemaGestao:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontePadrao = ("Arial", "12")
        self.janela.pack()

        self.titulo = Label(self.janela, text="")
        self.titulo.pack()
        self.titulo["font"] = ("Arial", 30, "bold")
        self.titulo.pack()

        # Frame para os botões centralizados
        self.janela5 = Frame(master)
        self.janela5.pack(expand=True, pady=20)  # Centraliza e adiciona espaço ao redor dos botões

        # Botões centralizados
        self.btn_usuarios = Button(self.janela5, text="Usuários", width=20, font=self.fontePadrao, command=self.abrir_usuarios)
        self.btn_usuarios.pack(pady=5)

        self.btn_cidades = Button(self.janela5, text="Cidades", width=20, font=self.fontePadrao, command=self.abrir_cidades)
        self.btn_cidades.pack(pady=5)

        self.btn_clientes = Button(self.janela5, text="Clientes", width=20, font=self.fontePadrao, command=self.abrir_clientes)
        self.btn_clientes.pack(pady=5)

        self.btn_fechar = Button(self.janela5, text="Fechar", width=20, font=self.fontePadrao, command=master.quit)
        self.btn_fechar.pack(pady=5)

    def abrir_usuarios(self):
        print("Abrir Usuários")

    def abrir_cidades(self):
        print("Abrir Cidades")

    def abrir_clientes(self):
        print("Abrir Clientes")


root = Tk()
root.title("Sistema de Gestão")
root.geometry("400x400")  # Define o tamanho da janela
SistemaGestao(root)
root.mainloop()