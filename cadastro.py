from livro import Livro
biblioteca = {}
def cadastro_livro():
        print("-" * 30)
        titulo = input("Digite o título do livro:").strip()
        autor = input("Digite o autor do livro:").strip()
        genero = input("Digite o gênero do livro:").strip()
        cadastro = Livro(titulo, autor, genero)
        biblioteca[titulo] = cadastro
        print(f"Livro '{titulo}' cadastrado com sucesso!\n\n")