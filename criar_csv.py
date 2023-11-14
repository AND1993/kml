# Importar biblioteca pandas para trabalhar com arquivos CSV
import pandas as pd

#importar biblioteca tkinter para  selecionar o caminho do arquivo
import tkinter as tk
from tkinter import filedialog


#função para abrir a tela de seleção do arquivo .csv
def selecionar_arquivo_csv():

    root = tk.Tk()
    root.withdraw()
    arquivo = filedialog.askopenfilename(filetypes=[('Arquivos CSV', '*.csv')])
    return arquivo

#função para selecionar o nome do candidato
def nome_saida():
    global nome
    nome = entry_nome.get()


    # Fecha a janela
    janela.destroy()

    # Criação da janela principal
    janela = tk.Tk()
    janela.title("Nome do candidato")

    # Criação do frame e do Label para o nome
    frame = tk.Frame(janela)
    frame.pack()
    label_nome = tk.Label(frame, text="Informe o nome do candidato")
    label_nome.pack(side=tk.LEFT)

    # Criação da Entry para inserir o nome
    entry_nome = tk.Entry(frame)
    entry_nome.pack(side=tk.LEFT)

    # Criação do botão para processar os dados
    button_processar = tk.Button(frame, text="Salvar", command=nome_saida)
    button_processar.pack(side=tk.LEFT)

    # Início do loop principal da janela
    janela.mainloop()

#NOme arquivo saida

def nome_saida():
    global saida
    saida = entry_nome.get()+".csv"


    # Fecha a janela
    janela.destroy()

    # Criação da janela principal
    janela = tk.Tk()
    janela.title("Arquivo de saida")

    # Criação do frame e do Label para o nome
    frame = tk.Frame(janela)
    frame.pack()
    label_nome = tk.Label(frame, text="Informe o nome do arquivo de saida")
    label_nome.pack(side=tk.LEFT)

    # Criação da Entry para inserir o nome
    entry_nome = tk.Entry(frame)
    entry_nome.pack(side=tk.LEFT)

    # Criação do botão para processar os dados
    button_processar = tk.Button(frame, text="Salvar", command=nome_saida)
    button_processar.pack(side=tk.LEFT)

    # Início do loop principal da janela
    janela.mainloop()

arquivo_entrada = selecionar_arquivo_csv()
arquivo_saida = saida

print(arquivo_entrada)
print(arquivo_saida)
print(nome)
