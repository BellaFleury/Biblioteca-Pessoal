
livros = {"lidos": [], "quero_ler": []}

def adicionar_lido(titulo):
    livros["lidos"].append(titulo)
    print(f'"{titulo}" adicionado aos lidos!')

def adicionar_quero_ler(titulo):
    livros["quero_ler"].append(titulo)
    print(f'"{titulo}" adicionado à lista de quero ler!')

def estatisticas():
    lidos = len(livros["lidos"])
    quero = len(livros["quero_ler"])
    total = lidos + quero
    pct = (lidos / total * 100) if total > 0 else 0

    print(f"\nestatísticas:")
    print(f"  lidos      : {lidos}")
    print(f"  quero ler  : {quero}")
    print(f"  total      : {total}")
    print(f"  progresso  : {pct:.0f}%")
