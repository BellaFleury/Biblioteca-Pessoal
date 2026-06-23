def ver_progressos():
    print("-" * 30)
    if not progressos:
        print("Nenhum progresso registrado ainda.\n")
        return

    for progresso in progressos.values():
        print(progresso)
        print()def registrar_progresso():
    print("-" * 30)
    if not biblioteca:
        print("Nenhum livro cadastrado ainda.\n")
        return

    print("Livros disponíveis:")
    for titulo in biblioteca:
        print(f"- {titulo}")

    titulo = input("\nDigite o título do livro: ").strip()

    if titulo not in biblioteca:
        print(f"Livro '{titulo}' não encontrado.\n")
        return

    livro = biblioteca[titulo]

    if titulo in progressos:
        progresso = progressos[titulo]
    else:
        total_paginas = int(input(f"Quantas páginas tem o livro '{titulo}'? "))
        progresso = ProgressoLeitura(livro, total_paginas)
        progressos[titulo] = progresso

    pagina = int(input(f"Em que página você parou? (0 a {progresso.total_paginas}) "))

    try:
        progresso.atualizar_pagina(pagina)
        print(f"\nProgresso atualizado!\n{progresso}\n")
    except ValueError as erro:
        print(f"Erro: {erro}\n")from cadastro import biblioteca

progressos = {}

class ProgressoLeitura:
    def __init__(self, livro, total_paginas):
        self.livro = livro
        self.total_paginas = total_paginas
        self.pagina_atual = 0

    def atualizar_pagina(self, pagina):
        if pagina < 0 or pagina > self.total_paginas:
            raise ValueError("Pagina invalida")
        self.pagina_atual = pagina

    def percentual_concluido(self):
        return round((self.pagina_atual / self.total_paginas) * 100, 1)

    def __str__(self):
        return f"Título: {self.livro.titulo} | Autor: {self.livro.autor}\nProgresso: {self.pagina_atual} de {self.total_paginas} páginas ({self.percentual_concluido()}% de 100%)"
