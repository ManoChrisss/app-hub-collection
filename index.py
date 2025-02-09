import tkinter as tk

class Index:
    def __init__(self, master):
        self.master = master
        self.master.title("Página Inicial")
        self.master.geometry("600x600")
        self.master.config(bg="black")

        # Adicionando o label com o texto acima do visor
        self.label = tk.Label(self.master, text="Bem-vindo! Escolha seu app abaixo:", font=("Arial", 14), bg="grey", fg="white", anchor="center")

        # Grid para o label
        self.label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Garantir que a coluna onde o label está fique expandida horizontalmente
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_columnconfigure(3, weight=1)

        # Botão para ir para a calculadora
        self.button = tk.Button(self.master, text="Calculadora", font=("Arial", 20), bg="grey", fg="white", width=15, height=2, command=self.open_calculator)
        self.button.grid(row=1, column=0, columnspan=4, padx=10, pady=20)

    def open_calculator(self):
    # Fecha a tela atual
        self.master.destroy()

    # Importa o arquivo da calculadora e cria uma nova janela
        import calculadora  # ou o nome correto do arquivo
        root = tk.Tk()
        self.calculator = calculadora.Calculator(root)
        root.mainloop()


