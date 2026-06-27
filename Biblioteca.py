from Livro import Livro

class Biblioteca:
    def __init__(self):
        self._livros = {}  # titulo -> Livro

    # ---------- Cadastro ----------
    def cadastrar(self, titulo, autor, genero, total_paginas=0):
        if titulo in self._livros:
            raise ValueError(f"Livro '{titulo}' já está cadastrado.")
        livro = Livro(titulo, autor, genero, total_paginas)
        self._livros[titulo] = livro
        return livro

    def remover(self, titulo):
        if titulo not in self._livros:
            raise KeyError(f"Livro '{titulo}' não encontrado.")
        del self._livros[titulo]

    # ---------- Consultas ----------
    def todos(self):
        return list(self._livros.values())

    def por_autor(self, autor):
        return [l for l in self._livros.values() if l.autor.lower() == autor.lower()]

    def por_genero(self, genero):
        return [l for l in self._livros.values() if l.genero.lower() == genero.lower()]

    def por_status(self, status):
        return [l for l in self._livros.values() if l.status == status]

    def buscar(self, titulo):
        return self._livros.get(titulo)

    # ---------- Estatísticas ----------
    def estatisticas(self):
        total = len(self._livros)
        lidos = len(self.por_status("lido"))
        lendo = len(self.por_status("lendo"))
        quero_ler = len(self.por_status("quero_ler"))
        pct = round((lidos / total * 100), 1) if total > 0 else 0.0

        avaliacoes = [
            l.get_avaliacao()["nota"]
            for l in self._livros.values()
            if l.get_avaliacao() is not None
        ]
        media_nota = round(sum(avaliacoes) / len(avaliacoes), 2) if avaliacoes else None

        generos = {}
        for l in self._livros.values():
            generos[l.genero] = generos.get(l.genero, 0) + 1

        return {
            "total": total,
            "lidos": lidos,
            "lendo": lendo,
            "quero_ler": quero_ler,
            "percentual_lido": pct,
            "media_avaliacao": media_nota,
            "por_genero": generos,
        }
