import tkinter as tk
from tkinter import messagebox
import random

class JogoDaForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca - TI 🎮")
        self.root.geometry("700x450")
        self.root.resizable(True, True)

 
        # Palavras do jogo em dicionário palavra -> dica
        self.palavras = {
            'python': 'Linguagem de programação muito usada em IA e automação',
            'java': 'Linguagem famosa pelo lema "write once, run anywhere"',
            'javascript': 'Linguagem essencial para web interativa',
            'typescript': 'Superset do JavaScript com tipagem estática',
            'ruby': 'Linguagem conhecida pelo framework Rails',
            'csharp': 'Linguagem da Microsoft usada em .NET',
            'php': 'Muito usada em sites dinâmicos e WordPress',
            'go': 'Linguagem criada pelo Google, muito rápida e leve',
            'kotlin': 'Linguagem oficial para Android',
            'swift': 'Linguagem oficial para iOS',
            'html': 'Linguagem de marcação para estruturar páginas web',
            'css': 'Usada para estilizar páginas web',
            'sql': 'Linguagem para manipulação de bancos de dados relacionais',
            'nosql': 'Banco de dados não relacional',
            'mongodb': 'Banco de dados NoSQL orientado a documentos',
            'mysql': 'Banco de dados relacional muito popular',
            'postgresql': 'Banco de dados relacional avançado e open source',
            'oracle': 'Banco de dados muito usado em empresas grandes',
            'docker': 'Ferramenta para containers',
            'kubernetes': 'Orquestrador de containers',
            'linux': 'Sistema operacional open source',
            'windows': 'Sistema operacional da Microsoft',
            'ubuntu': 'Distribuição Linux popular',
            'git': 'Sistema de controle de versão',
            'github': 'Plataforma de hospedagem de código',
            'gitlab': 'Alternativa ao GitHub',
            'versionamento': 'Processo de manter histórico de código',
            'algoritmo': 'Sequência de passos para resolver um problema',
            'compilador': 'Transforma código fonte em código executável',
            'interpretador': 'Executa código sem compilar antes',
            'framework': 'Conjunto de ferramentas para desenvolvimento',
            'biblioteca': 'Coleção de funções e códigos reutilizáveis',
            'api': 'Interface para comunicação entre sistemas',
            'rest': 'Estilo de arquitetura de APIs',
            'graphql': 'Alternativa ao REST para APIs flexíveis',
            'json': 'Formato leve de troca de dados',
            'xml': 'Formato de dados mais verboso que JSON',
            'rede': 'Conjunto de computadores conectados',
            'servidor': 'Computador que fornece recursos ou serviços',
            'cliente': 'Dispositivo que consome serviços de um servidor',
            'backend': 'Parte do sistema que roda no servidor',
            'frontend': 'Parte do sistema que roda no navegador',
            'fullstack': 'Dev que trabalha com front e back',
            'cloud': 'Computação em nuvem',
            'aws': 'Serviço de nuvem da Amazon',
            'azure': 'Serviço de nuvem da Microsoft',
            'googlecloud': 'Serviço de nuvem do Google'
        }

        self.reset_game()

        # Label de instrução
        self.label_info = tk.Label(root, text="Adivinhe a palavra relacionada a TI:", font=("Arial", 14))
        self.label_info.pack(pady=10)
        self.label_dica = tk.Label(root, text=f"Dica: {self.dica}", font=("Arial", 12), fg="gray")
        self.label_dica.pack(pady=5)


        # Exibição da palavra oculta
        self.label_palavra = tk.Label(root, text=" ".join(self.palavra_oculta), font=("Courier", 20))
        self.label_palavra.pack(pady=10)

        # Entrada para digitar letra
        self.entry_letra = tk.Entry(root, font=("Arial", 14), width=5, justify="center")
        self.entry_letra.pack(pady=10)

        # Botão para tentar letra
        self.btn_tentar = tk.Button(root, text="Tentar", font=("Arial", 12), command=self.tentar)
        self.btn_tentar.pack(pady=5)

        # Label de tentativas restantes
        self.label_tentativas = tk.Label(root, text=f"Tentativas restantes: {self.tentativas}", font=("Arial", 12))
        self.label_tentativas.pack(pady=10)

        # Botão de novo jogo
        self.btn_novo = tk.Button(root, text="Novo Jogo", font=("Arial", 12), command=self.novo_jogo)
        self.btn_novo.pack(pady=10)
        # Botão para voltar ao menu principal
        self.btn_voltar = tk.Button(root, text="Voltar", font=("Arial", 12), command=self.sair)
        self.btn_voltar.pack(pady=5)

    def reset_game(self):
        # Sorteia uma palavra e sua dica
        self.palavra, self.dica = random.choice(list(self.palavras.items()))
        self.palavra = self.palavra.lower()
        self.palavra_oculta = ["*" for _ in self.palavra]
        self.tentativas = 6


    def tentar(self):
        letra = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)

        if not letra or len(letra) != 1:
            messagebox.showwarning("Aviso", "Digite apenas UMA letra!")
            return

        if letra in self.palavra:
            for indice, caracter in enumerate(self.palavra):
                if caracter == letra:
                    self.palavra_oculta[indice] = letra
        else:
            self.tentativas -= 1

        # Atualiza os labels
        self.label_palavra.config(text=" ".join(self.palavra_oculta))
        self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")

        # Checa vitória ou derrota
        if "*" not in self.palavra_oculta:
            messagebox.showinfo("Vitória!", "Parabéns! Você ganhou!")
            self.novo_jogo()
        elif self.tentativas == 0:
            messagebox.showerror("Game Over", f"Você perdeu! A palavra era: {self.palavra}")
            self.novo_jogo()

    def novo_jogo(self):
        self.reset_game()
        self.label_palavra.config(text=" ".join(self.palavra_oculta))
        self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")
        self.label_dica.config(text=f"Dica: {self.dica}")

    def sair(self):
        self.root.destroy()
        import index  # Importando a tela inicial (index.py)
        root = tk.Tk()
        index.Index(root)  # Chama a classe da tela inicial
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoDaForca(root)
    root.mainloop()
