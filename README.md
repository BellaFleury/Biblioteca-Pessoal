# Biblioteca-Pessoal
## (Biblioteca Pessoal)

O módulo de avaliações permite gerenciar notas e comentários de forma individual para cada livro.

### Funcionalidades
* **Avaliação Única:** O usuário atribui uma nota (1 a 5) e um comentário por livro.
* **Sobrescrita Automática:** Avaliar um livro novamente substitui os dados antigos automaticamente.
* **Exibição:** Mostra a nota formatada e omite o comentário caso esteja em branco.

### Métodos da Classe `Livro`

* `adicionar_avaliacao(nota, comentario)`: Salva ou atualiza a avaliação.
* `exibir_avaliacao()`: Mostra a nota e o comentário no terminal.
