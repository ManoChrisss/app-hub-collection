import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("390x700")
        self.master.config(bg="black")

        self.result_var = tk.StringVar()

        # Label com instrução acima do visor
        self.label = tk.Label(
            self.master,
            text="Faça sua conta matemática",
            font=("Arial", 14),
            bg="black",
            fg="white"
        )
        self.label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Campo de entrada (visor)
        self.entry = tk.Entry(
            self.master,
            textvariable=self.result_var,
            justify="right",
            font=("Arial", 24)
        )
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # Criar botões
        self.criar_botoes()

    def criar_botoes(self):
        buttons = [
            ("C", 2, 0), ("**", 2, 1), ("%", 2, 2), ("/", 2, 3),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
            ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("-", 4, 3),
            ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("+", 5, 3),
            ("=", 6, 0), ("0", 6, 1), (".", 6, 2), ("SAIR", 6, 3)
        ]

        for texto, row, col in buttons:
            if texto == "=":
                button = tk.Button(
                    self.master,
                    text=texto,
                    font=("Arial", 22),
                    bg="grey",
                    fg="white",
                    width=5,
                    height=2,
                    command=self.calcular
                )
            elif texto == "C":
                button = tk.Button(
                    self.master,
                    text=texto,
                    font=("Arial", 22),
                    bg="grey",
                    fg="white",
                    width=5,
                    height=2,
                    command=self.limpar
                )
            elif texto == "SAIR":
                button = tk.Button(
                    self.master,
                    text=texto,
                    font=("Arial", 22),
                    bg="grey",
                    fg="white",
                    width=5,
                    height=2,
                    command=self.master.destroy  # Sai do app
                )
            else:
                button = tk.Button(
                    self.master,
                    text=texto,
                    font=("Arial", 22),
                    bg="grey",
                    fg="white",
                    width=5,
                    height=2,
                    command=lambda t=texto: self.append(t)
                )

            button.grid(row=row, column=col, padx=1, pady=1)

    def append(self, texto):
        current = self.result_var.get()
        self.result_var.set(current + texto)

    def calcular(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(str(result))
        except Exception:
            self.result_var.set("Error")

    def limpar(self):
        self.result_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
