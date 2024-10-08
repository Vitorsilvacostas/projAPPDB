import tkinter as tk
from tkinter import *

class SistemaGestao:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontePadrao = ("Arial", "12")
        self.janela.pack()

        self.titulo = Label(self.janela, text="Informe os dados")
        self.titulo["font"] = ("Arial", 20, "bold")
        self.titulo.pack(pady=20)

        self.janela_campos = Frame(master)
        self.janela_campos.pack(pady=10)

        self.idUsuarioLabel = Label(self.janela_campos, text="ID Usuário:", font=self.fontePadrao)
        self.idUsuarioLabel.grid(row=0, column=0, padx=5, pady=5, sticky=E)
        self.idUsuario = Entry(self.janela_campos)
        self.idUsuario.grid(row=0, column=1, padx=5, pady=5)

        self.btn_buscar = Button(self.janela_campos, text="Buscar", font=self.fontePadrao, command=self.buscar_usuario)
        self.btn_buscar.grid(row=0, column=2, padx=5, pady=5)  # Botão Buscar adicionado ao lado de ID Usuário

        self.nomeLabel = Label(self.janela_campos, text="Nome:", font=self.fontePadrao)
        self.nomeLabel.grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self.nome = Entry(self.janela_campos)
        self.nome.grid(row=1, column=1, padx=5, pady=5)

        self.telefoneLabel = Label(self.janela_campos, text="Telefone:", font=self.fontePadrao)
        self.telefoneLabel.grid(row=2, column=0, padx=5, pady=5, sticky=E)
        self.telefone = Entry(self.janela_campos)
        self.telefone.grid(row=2, column=1, padx=5, pady=5)

        self.emailLabel = Label(self.janela_campos, text="Email:", font=self.fontePadrao)
        self.emailLabel.grid(row=3, column=0, padx=5, pady=5, sticky=E)
        self.email = Entry(self.janela_campos)
        self.email.grid(row=3, column=1, padx=5, pady=5)

        self.usuarioLabel = Label(self.janela_campos, text="Usuário:", font=self.fontePadrao)
        self.usuarioLabel.grid(row=4, column=0, padx=5, pady=5, sticky=E)
        self.usuario = Entry(self.janela_campos)
        self.usuario.grid(row=4, column=1, padx=5, pady=5)

        self.senhaLabel = Label(self.janela_campos, text="Senha:", font=self.fontePadrao)
        self.senhaLabel.grid(row=5, column=0, padx=5, pady=5, sticky=E)
        self.senha = Entry(self.janela_campos, show="*")
        self.senha.grid(row=5, column=1, padx=5, pady=5)

        self.janela_botoes = Frame(master)
        self.janela_botoes.pack(pady=20)

        self.btn_inserir = Button(self.janela_botoes, text="Inserir", font=self.fontePadrao, width=10, command=self.inserir_dados)
        self.btn_inserir.grid(row=0, column=0, padx=5)

        self.btn_alterar = Button(self.janela_botoes, text="Alterar", font=self.fontePadrao, width=10, command=self.alterar_dados)
        self.btn_alterar.grid(row=0, column=1, padx=5)

        self.btn_excluir = Button(self.janela_botoes, text="Excluir", font=self.fontePadrao, width=10, command=self.excluir_dados)
        self.btn_excluir.grid(row=0, column=2, padx=5)

    def buscar_usuario(self):
        print("Buscar usuário")

    def inserir_dados(self):
        print("Inserir dados")

    def alterar_dados(self):
        print("Alterar dados")

    def excluir_dados(self):
        print("Excluir dados")

root = Tk()
root.title("Sistema de Gestão")
root.geometry("400x400")
SistemaGestao(root)
root.mainloop()
