Livro
class Livro:
    def __init__(self, titulo, autor, genero, total_paginas=0, status="quero_ler"):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.total_paginas = total_paginas
        self.status = status  # "quero_ler", "lendo", "lido"
        self.pagina_atual = 0
        self.__avaliacao = None

    # ---------- Progresso ----------
    def atualizar_pagina(self, pagina):
        if pagina < 0 or pagina > self.total_paginas:
            raise ValueError(f"Página inválida. Deve ser entre 0 e {self.total_paginas}.")
        self.pagina_atual = pagina
        if self.total_paginas > 0 and pagina == self.total_paginas:
            self.status = "lido"
        elif pagina > 0:
            self.status = "lendo"

    def percentual_concluido(self):
        if self.total_paginas == 0:
            return 0.0
        return round((self.pagina_atual / self.total_paginas) * 100, 1)

    # ---------- Avaliação ----------
    def adicionar_avaliacao(self, nota, comentario=""):
        if not (1 <= nota <= 5):
            raise ValueError("A nota deve ser um número entre 1 e 5.")
        self.__avaliacao = {
            "nota": nota,
            "comentario": comentario.strip()
        }

    def get_avaliacao(self):
        return self.__avaliacao

    # ---------- Representação ----------
    def __str__(self):
        nota = f"{self.__avaliacao['nota']}/5" if self.__avaliacao else "Não avaliado"
        return (
            f"Título: {self.titulo} | Autor: {self.autor} | "
            f"Gênero: {self.genero} | Avaliação: {nota}"
        )