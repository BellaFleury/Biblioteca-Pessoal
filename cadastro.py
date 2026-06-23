from livro import Livro
biblioteca = {}
print("CADASTRO DE LIVROS")
print("-" * 30)
while True:
    print("-" * 30)
    titulo = input("Digite o título do livro:").strip()
    autor = input("Digite o autor do livro:").strip()
    genero = input("Digite o gênero do livro:").strip()
    cadastro = Livro(titulo, autor, genero)
    biblioteca[titulo] = cadastro
    print(f"Livro '{titulo}' cadastrado com sucesso!\n\n")
    continuar = input("se deseja parar de cadastrar livros digite 0, para continuar digite qualquer outra tecla: ")
    if continuar == "0":
        break
print("\n\nLIVROS CADASTRADOS")
for livro in biblioteca.values():
    print(livro)