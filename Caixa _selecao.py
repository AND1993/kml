import tkinter as tk

def exibir_caixa_selecao():
    root = tk.Tk()
    root.title('Selecione uma opção')
    root.geometry('300x150')
    root.resizable(False, False)

    var_prefeito = tk.BooleanVar()
    var_vereador = tk.BooleanVar()
    contador = 0

    checkbutton_prefeito = tk.Checkbutton(root, text='Prefeito', variable=var_prefeito)
    checkbutton_vereador = tk.Checkbutton(root, text='Vereador', variable=var_vereador)

    checkbutton_prefeito.pack(pady=10)
    checkbutton_vereador.pack(pady=10)

    filename = filedialog.askopenfilename(title="Selecione um arquivo")

    def selecionar():
        if var_prefeito.get() and var_vereador.get():
            contador = 3
        elif var_prefeito.get():
            contador = 2
        elif var_vereador.get():
            contador = 1
        else:
            print('Nenhuma opção selecionada.')


        root.destroy()

    button_selecionar = tk.Button(root, text='Confirma', command=selecionar)
    button_selecionar.pack(pady=10)

    root.mainloop()

    print(contador)

# Exemplo de uso:
exibir_caixa_selecao()
