import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon='🏠',    
)


#with open('estilo.css') as estilo:
    #st.markdown(f'<style>{estilo.read()}</style>', unsafe_allow_html=True)


st.sidebar.divider()
st.sidebar.page_link('pages/1_faturamento.py', label='Faturamento', icon='💲')

def main():

    st.cache_data.clear()
    st.cache_resource.clear()
    st.session_state.clear()

    with st.container(border=True):
    
        st.title('Precificador Varejista')

        st.markdown(
            """
            Ferramenta voltada para o gestor varejista no suporte à precificação de produtos e ponto de equilíbrio.
            \nClique em > para abrir a barra lateral em depois clique em 💲Faturamento para iniciar, ou saiba mais abaixo:

            """)
        with st.expander(label='Entenda os conceitos básicos e aprenda o passo a passo',expanded=False):
            st.markdown("""
                        Objetivos: 
                        encontrar o markup para precificação dos produtos;
                        encontrar o ponto de equilíbrio.                        
                        
                        O que é markup?
                        O que é ponto de equilíbrio?
                        Como é feito o cálculo?
                        
                        Passo a passo:""")

main()
