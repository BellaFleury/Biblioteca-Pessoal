class Livro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.__avaliacao = None

    def adicionar_avaliacao(self, nota, comentario=""):
        if 1 <= nota <= 5:
            self.__avaliacao = {
                "nota": nota,
                "comentario": comentario.strip()
            }
            print(f"Avaliação salva com sucesso para o livro '{self.titulo}'!")
            return True

        print("Erro: A nota deve ser um número inteiro entre 1 e 5.")
        return False

    def exibir_avaliacao(self):
        print(f"\n===== AVALIAÇÃO DE '{self.titulo.upper()}' =====")

        if self.__avaliacao is None:
            print("Você ainda não avaliou este livro.")
            print("===========================================")
            return

        nota = self.__avaliacao["nota"]
        texto = self.__avaliacao["comentario"]

        if texto:
            print(f"Nota: {nota}/5")
            print(f"Comentário: {texto}")
        else:
            print(f"Nota: {nota}/5 (Sem comentário em texto)")

        print("===========================================")

    def __str__(self):
        status_nota = f"{self.__avaliacao['nota']}/5" if self.__avaliacao else "Não avaliado"
        return f"Título: {self.titulo} | Autor: {self.autor} | Gênero: {self.genero} | Sua Avaliação: {status_nota}"