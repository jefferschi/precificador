import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon='',
    
)

st.sidebar.page_link('pages/faturamento.py', label='Faturamento', icon='💲')

def main():


    st.title('Precificador Varejista')

    st.markdown(
        """
        Ferramenta voltada para o empresário varejista para a precificação de produtos e análise de rentabilidade.
        
        Como usar:

        """
    )



main()
