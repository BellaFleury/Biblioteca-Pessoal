import streamlit as st
import pandas as pd
import altair as alt
from Biblioteca import Biblioteca

# ── Configuração da página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Biblioteca Pessoal",
    page_icon="assets/favicon.png",
    layout="wide",
)

# ── Carrega CSS externo ─────────────────────────────────────────────────────
def carregar_css(nome_arquivo):
    with open(nome_arquivo, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

carregar_css("style.css")

# ── Estado da sessão ────────────────────────────────────────────────────────
if "bib" not in st.session_state:
    bib = Biblioteca()
    bib.cadastrar("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 1200)
    bib.cadastrar("1984", "George Orwell", "Distopia", 328)
    bib.cadastrar("Dom Casmurro", "Machado de Assis", "Romance", 256)
    bib.cadastrar("Duna", "Frank Herbert", "Ficção Científica", 688)
    bib.buscar("1984").atualizar_pagina(328)
    bib.buscar("1984").adicionar_avaliacao(5, "Clássico indispensável.")
    bib.buscar("Dom Casmurro").atualizar_pagina(256)
    bib.buscar("Dom Casmurro").adicionar_avaliacao(4, "Capitu era culpada? Nunca saberemos.")
    bib.buscar("O Senhor dos Anéis").atualizar_pagina(420)
    st.session_state.bib = bib

bib = st.session_state.bib

# ── Helpers ─────────────────────────────────────────────────────────────────
STATUS_LABEL = {"lido": "Lido", "lendo": "Lendo", "quero_ler": "Quero ler"}
ESTRELAS = {1: "★☆☆☆☆", 2: "★★☆☆☆", 3: "★★★☆☆", 4: "★★★★☆", 5: "★★★★★"}

def badge(status):
    return f'<span class="badge badge-{status}">{STATUS_LABEL[status]}</span>'

def render_card(livro):
    av = livro.get_avaliacao()
    nota_html = f"&nbsp;&nbsp;{ESTRELAS[av['nota']]}" if av else ""
    pct = livro.percentual_concluido()
    progresso_html = f"<div class='card-meta' style='margin-top:4px;'>Progresso: {pct}% ({livro.pagina_atual}/{livro.total_paginas} págs)</div>" if livro.total_paginas > 0 else ""
    comentario_html = f"<div class='card-meta' style='font-style:italic;margin-top:2px;'>\"{av['comentario']}\"</div>" if av and av['comentario'] else ""
    st.markdown(f"""
    <div class="card">
        <div class="card-titulo">{livro.titulo}{badge(livro.status)}{nota_html}</div>
        <div class="card-meta">{livro.autor} &nbsp;·&nbsp; {livro.genero}</div>
        {progresso_html}
        {comentario_html}
    </div>
    """, unsafe_allow_html=True)

def titulo_pagina(imagem, texto):
    col_img, col_txt = st.columns([1, 10])
    with col_img:
        st.image(imagem, width= 180)
    with col_txt:
        st.title(texto)
    st.markdown("---")

# ── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("assets/logo.png", width=220)
    st.markdown("---")
    pagina = st.radio(
        "Navegar",
        ["Início", "Cadastrar livro", "Meus livros", "Atualizar progresso", "Avaliar livro", "Estatísticas"],
        label_visibility="collapsed"
    )

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA: INÍCIO
# ════════════════════════════════════════════════════════════════════════════
if pagina == "Início":
    titulo_pagina("assets/home.png", "Minha Biblioteca Pessoal")
    st.markdown("Organize seus livros, acompanhe suas leituras e descubra seus hábitos literários.")
    st.markdown("<br>", unsafe_allow_html=True)

    stats = bib.estatisticas()
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="stat-box"><div class="stat-num">{stats["total"]}</div><div class="stat-label">Total de livros</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-box"><div class="stat-num">{stats["lidos"]}</div><div class="stat-label">Livros lidos</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="stat-box"><div class="stat-num">{stats["lendo"]}</div><div class="stat-label">Lendo agora</div></div>', unsafe_allow_html=True)
    with c4:
        nota = f'{stats["media_avaliacao"]} ★' if stats["media_avaliacao"] else "—"
        st.markdown(f'<div class="stat-box"><div class="stat-num">{nota}</div><div class="stat-label">Nota média</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("### Lendo agora")
        lendo = bib.por_status("lendo")
        if lendo:
            for l in lendo:
                render_card(l)
        else:
            st.info("Nenhum livro em andamento.")
    with col_r:
        st.markdown("### Últimos lidos")
        lidos = bib.por_status("lido")
        if lidos:
            for l in lidos[:3]:
                render_card(l)
        else:
            st.info("Nenhum livro marcado como lido ainda.")

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA: CADASTRAR
# ════════════════════════════════════════════════════════════════════════════
elif pagina == "Cadastrar livro":
    titulo_pagina("assets/add.png", "Cadastrar novo livro")

    with st.form("form_cadastro", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            titulo = st.text_input("Título *")
            autor  = st.text_input("Autor *")
        with col2:
            genero  = st.text_input("Gênero *")
            paginas = st.number_input("Total de páginas", min_value=0, value=0, step=1)
        submitted = st.form_submit_button("Cadastrar livro", use_container_width=True)

    if submitted:
        if not titulo or not autor or not genero:
            st.error("Preencha título, autor e gênero.")
        else:
            try:
                bib.cadastrar(titulo.strip(), autor.strip(), genero.strip(), int(paginas))
                st.success(f"**{titulo}** cadastrado com sucesso!")
                st.balloons()
            except ValueError as e:
                st.error(str(e))

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA: MEUS LIVROS
# ════════════════════════════════════════════════════════════════════════════
elif pagina == "Meus livros":
    titulo_pagina("assets/books.png", "Meus livros")

    todos = bib.todos()
    if not todos:
        st.info("Nenhum livro cadastrado ainda. Vá em Cadastrar livro para começar!")
        st.stop()

    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        filtro_status = st.selectbox("Filtrar por status", ["Todos", "Lido", "Lendo", "Quero ler"])
    with col_f2:
        autores = sorted(set(l.autor for l in todos))
        filtro_autor = st.selectbox("Filtrar por autor", ["Todos"] + autores)
    with col_f3:
        generos = sorted(set(l.genero for l in todos))
        filtro_genero = st.selectbox("Filtrar por gênero", ["Todos"] + generos)

    resultado = todos
    if filtro_status != "Todos":
        mapa = {"Lido": "lido", "Lendo": "lendo", "Quero ler": "quero_ler"}
        resultado = [l for l in resultado if l.status == mapa[filtro_status]]
    if filtro_autor != "Todos":
        resultado = [l for l in resultado if l.autor == filtro_autor]
    if filtro_genero != "Todos":
        resultado = [l for l in resultado if l.genero == filtro_genero]

    st.markdown(f"**{len(resultado)} livro(s) encontrado(s)**")
    if resultado:
        for livro in resultado:
            render_card(livro)
    else:
        st.info("Nenhum livro encontrado com esses filtros.")

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA: ATUALIZAR PROGRESSO
# ════════════════════════════════════════════════════════════════════════════
elif pagina == "Atualizar progresso":
    titulo_pagina("assets/progress.png", "Atualizar progresso de leitura")

    todos = bib.todos()
    if not todos:
        st.info("Cadastre livros primeiro.")
        st.stop()

    titulo_sel = st.selectbox("Selecione o livro", [l.titulo for l in todos])
    livro = bib.buscar(titulo_sel)

    if livro:
        st.markdown(f"**Autor:** {livro.autor} &nbsp;|&nbsp; **Gênero:** {livro.genero}", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if livro.total_paginas == 0:
                total = st.number_input("Total de páginas do livro", min_value=1, step=1, value=100)
            else:
                total = livro.total_paginas
                st.metric("Total de páginas", total)
        with col2:
            pagina_nova = st.number_input("Página atual", min_value=0, max_value=int(total), value=int(livro.pagina_atual), step=1)

        pct_preview = round((pagina_nova / total * 100), 1) if total > 0 else 0
        st.progress(pct_preview / 100, text=f"{pct_preview}% concluído")

        if st.button("Salvar progresso", use_container_width=True):
            try:
                if livro.total_paginas == 0:
                    livro.total_paginas = int(total)
                livro.atualizar_pagina(int(pagina_nova))
                if livro.status == "lido":
                    st.success(f"Parabéns! Você terminou **{livro.titulo}**!")
                    st.balloons()
                else:
                    st.success(f"Progresso salvo: {pagina_nova}/{int(total)} páginas ({pct_preview}%)")
            except ValueError as e:
                st.error(str(e))

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA: AVALIAR LIVRO
# ════════════════════════════════════════════════════════════════════════════
elif pagina == "Avaliar livro":
    titulo_pagina("assets/star.png", "Avaliar livro")

    todos = bib.todos()
    if not todos:
        st.info("Cadastre livros primeiro.")
        st.stop()

    titulo_sel = st.selectbox("Selecione o livro", [l.titulo for l in todos])
    livro = bib.buscar(titulo_sel)

    if livro:
        av_atual = livro.get_avaliacao()
        if av_atual:
            st.info(f"Avaliação atual: {ESTRELAS[av_atual['nota']]}  ·  \"{av_atual['comentario']}\"")
        nota = st.slider("Nota (1 a 5)", min_value=1, max_value=5, value=av_atual["nota"] if av_atual else 3)
        st.markdown(f"### {ESTRELAS[nota]}")
        comentario = st.text_area("Comentário (opcional)", value=av_atual["comentario"] if av_atual else "", placeholder="O que você achou do livro?")

        if st.button("Salvar avaliação", use_container_width=True):
            try:
                livro.adicionar_avaliacao(nota, comentario)
                st.success(f"Avaliação de **{livro.titulo}** salva com sucesso!")
            except ValueError as e:
                st.error(str(e))

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA: ESTATÍSTICAS
# ════════════════════════════════════════════════════════════════════════════
elif pagina == "Estatísticas":
    titulo_pagina("assets/stats.png", "Estatísticas da biblioteca")

    stats = bib.estatisticas()
    if stats["total"] == 0:
        st.info("Cadastre livros para ver as estatísticas.")
        st.stop()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="stat-box"><div class="stat-num">{stats["total"]}</div><div class="stat-label">Total de livros</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-box"><div class="stat-num">{stats["percentual_lido"]}%</div><div class="stat-label">Da lista lida</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="stat-box"><div class="stat-num">{stats["lendo"]}</div><div class="stat-label">Em andamento</div></div>', unsafe_allow_html=True)
    with c4:
        nota = f'{stats["media_avaliacao"]} ★' if stats["media_avaliacao"] else "—"
        st.markdown(f'<div class="stat-box"><div class="stat-num">{nota}</div><div class="stat-label">Nota média</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_esq, col_dir = st.columns(2)

    with col_esq:
        st.markdown("### Status dos livros")
        status_data = pd.DataFrame({
            "Status": ["Lidos", "Lendo", "Quero ler"],
            "Quantidade": [stats["lidos"], stats["lendo"], stats["quero_ler"]]
        })
        chart = alt.Chart(status_data).mark_arc(innerRadius=60).encode(
            theta=alt.Theta("Quantidade:Q"),
            color=alt.Color("Status:N", scale=alt.Scale(
                domain=["Lidos", "Lendo", "Quero ler"],
                range=["#EB7347", "#FFA85D", "#FEC89A"]
            )),
            tooltip=["Status", "Quantidade"]
        ).properties(height=280)
        st.altair_chart(chart, use_container_width=True)

    with col_dir:
        st.markdown("### Livros por gênero")
        if stats["por_genero"]:
            genero_data = pd.DataFrame({
                "Gênero": list(stats["por_genero"].keys()),
                "Quantidade": list(stats["por_genero"].values())
            }).sort_values("Quantidade", ascending=True)
            bar = alt.Chart(genero_data).mark_bar(color="#EB7347", cornerRadiusTopRight=4, cornerRadiusBottomRight=4).encode(
                x=alt.X("Quantidade:Q", axis=alt.Axis(tickMinStep=1)),
                y=alt.Y("Gênero:N", sort="-x"),
                tooltip=["Gênero", "Quantidade"]
            ).properties(height=280)
            st.altair_chart(bar, use_container_width=True)

    st.markdown("### Progresso individual")
    livros_com_paginas = [l for l in bib.todos() if l.total_paginas > 0]
    if livros_com_paginas:
        for livro in livros_com_paginas:
            pct = livro.percentual_concluido()
            st.markdown(f"**{livro.titulo}** — {livro.pagina_atual}/{livro.total_paginas} págs")
            st.progress(pct / 100, text=f"{pct}%")
    else:
        st.info("Nenhum livro com número de páginas definido.")
