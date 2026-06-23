class Livro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Gênero: {self.genero}"