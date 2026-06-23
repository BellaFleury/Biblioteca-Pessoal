from livro import Livro
from cadastro import cadastro_livro,biblioteca
print("CADASTRO DE LIVROS")
print("-" * 30)
while True:
    cadastro_livro()
    continuar = input("se deseja parar de cadastrar livros digite 0, para continuar digite qualquer outra tecla: ")
    if continuar == "0":
        break
print("\nLivros cadastrados:")
for livro in biblioteca.values():
    print(livro)