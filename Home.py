import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon='🏠',    
    initial_sidebar_state="expanded",
)

# arquivo css
with open('estilo.css') as estilo:
    st.markdown(f'<style>{estilo.read()}</style>', unsafe_allow_html=True)

# barra lateral
st.sidebar.divider()
st.sidebar.page_link('pages/1_faturamento.py', label='Faturamento', icon='💲')


# função principal
def main():

    # limpa os campos, estados da sessão e o cache
    st.cache_data.clear()
    st.cache_resource.clear()
    st.session_state.clear()

    with st.container(border=True):
    
        st.write('<h1>Precificador Varejista</h1>', unsafe_allow_html=True)
        st.divider()

        st.markdown(
            """
            <h3> Ferramenta de suporte ao gestor varejista para a precificação de produtos e encontro do ponto de equilíbrio.</h3>
            <h4> Na barra lateral clique em 💲Faturamento para iniciar, ou saiba mais abaixo:</h4)
            
            """,unsafe_allow_html=True)
        
        with st.expander(label='Entenda os conceitos básicos e aprenda o passo a passo',expanded=False):
            st.markdown("""
                        <p class="expandido"> Para que o cálculo funione de forma correta,
                                                observe a sequência de telas. Sempre no final de cada etapa 
                            aparecerá uma mensagem informando qual é a tela seguinte.<br>
                            Mas não se preocupe, a próxima tela será liberada somente quando a etapa atual for 
                            concluída.😊<br>
                        </p>
                        
                        <p class="expandido">                        
                            🤷🏻‍♂️<b>O que é markup?</b>🏷️<br>
                            O markup é uma técnica utilizada para precificar produtos. Ele representa a diferença entre o custo de 
                            um produto e o seu preço de venda. Especificamente, o markup é calculado como a proporção entre o lucro 
                            bruto desejado e o custo do produto.<br>
                            O markup pode variar dependendo do setor, da concorrência, da demanda do mercado e de outros fatores. 
                            Ele é uma ferramenta importante para garantir que os produtos sejam precificados de forma a garantir 
                            uma margem de lucro adequada para o negócio.
                        <p>
                        <p class="expandido">                            
                            🤷🏻‍♂️<b>O que é ponto de equilíbrio?</b>⚖️<br>
                            Ele representa o ponto no qual as receitas totais se igualam aos custos totais, resultando em um lucro líquido igual a zero. Em outras palavras, é o momento em que uma empresa não está gerando lucro nem prejuízo.
                            
                        </p>
                        """, unsafe_allow_html=True)

main()
