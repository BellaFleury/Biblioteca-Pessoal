from cadastro import biblioteca

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
