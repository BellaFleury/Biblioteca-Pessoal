class Livro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.genero})"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def filtrar_por_autor(self, autor):
        return [
            livro for livro in self.livros
            if livro.autor.lower() == autor.lower()
        ]

    def filtrar_por_genero(self, genero):
        return [
            livro for livro in self.livros
            if livro.genero.lower() == genero.lower()
        ]

    def filtrar_por_autor_e_genero(self, autor, genero):
        return [
            livro for livro in self.livros
            if livro.autor.lower() == autor.lower()
            and livro.genero.lower() == genero.lower()
        ]


# Criando a biblioteca
biblioteca = Biblioteca()

biblioteca.adicionar_livro(Livro("Dom Casmurro", "Machado de Assis", "Romance"))
biblioteca.adicionar_livro(Livro("Memórias Póstumas", "Machado de Assis", "Romance"))
biblioteca.adicionar_livro(Livro("O Hobbit", "J.R.R. Tolkien", "Fantasia"))
biblioteca.adicionar_livro(Livro("Harry Potter", "J.K. Rowling", "Fantasia"))

# Menu
print("\n=== FILTRO DE LIVROS ===")
print("1 - Filtrar por autor")
print("2 - Filtrar por gênero")
print("3 - Filtrar por autor e gênero")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    autor = input("Digite o autor: ")
    resultados = biblioteca.filtrar_por_autor(autor)

elif opcao == "2":
    genero = input("Digite o gênero: ")
    resultados = biblioteca.filtrar_por_genero(genero)

elif opcao == "3":
    autor = input("Digite o autor: ")
    genero = input("Digite o gênero: ")
    resultados = biblioteca.filtrar_por_autor_e_genero(autor, genero)

else:
    print("Opção inválida!")
    resultados = []

print("\n=== RESULTADOS ===")

if resultados:
    for livro in resultados:
        print(livro)
else:
    print("Nenhum livro encontrado.")