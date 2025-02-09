import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("390x700")
        self.master.config(bg="black")

        self.result_var = tk.StringVar()

        # Adicionando o label com o texto acima do visor
        self.label = tk.Label(self.master, text="Faça sua conta matemática!", font=("Arial", 14), bg="black", fg="white")
        self.label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Criando o campo de entrada (visor)
        self.entry = tk.Entry(self.master, textvariable=self.result_var, justify="right", font=("Arial", 24))
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()


    def create_buttons(self):
        buttons = [
            ("C", 2, 0), ("**", 2, 1), ("%", 2, 2), ("/", 2, 3),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
            ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("-", 4, 3),
            ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("+", 5, 3),
            ("=", 6, 0), ("0", 6, 1), (".", 6, 2), ("SAIR", 6, 3)
        ]

        for text, row, col in buttons:
            if text == "=":
                button = tk.Button(self.master, text=text, font=("Arial", 22), bg="grey", fg="white", width=5, height=2, command=self.evaluate)
            elif text == "C":
                button = tk.Button(self.master, text=text, font=("Arial", 22),bg="grey", fg="white", width=5, height=2, command=self.clear)
            elif text == "SAIR":
                button = tk.Button(self.master, text=text, font=("Arial", 22), bg="grey", fg="white", width=5, height=2, command=self.go_back_to_index)
            else:
                button = tk.Button(self.master, text=text, font=("Arial", 22), bg="grey", fg="white", width=5, height=2, command=lambda text=text: self.append(text))

            button.grid(row=row, column=col, padx=1, pady=1)

    def append(self, text):
        current = self.result_var.get()
        self.result_var.set(current + text)

    def evaluate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(str(result))
        except Exception:
            self.result_var.set("Error")
            
    def clear(self):
        self.result_var.set("")

    def go_back_to_index(self):
        self.master.destroy()
        import index  # Importando a tela inicial (index.py)
        root = tk.Tk()
        index.Index(root)  # Chama a classe da tela inicial
        root.mainloop()

