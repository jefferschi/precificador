import streamlit as st

import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Markup",
    page_icon='🏷️',
  
    )

with open('estilo.css') as estilo:
    st.markdown(f'<style>{estilo.read()}</style>', unsafe_allow_html=True)

st.sidebar.page_link('Home.py', label='Home', icon='🏠')
st.sidebar.page_link('pages/3_custos_variaveis.py', label='Custos Variáveis', icon='➗')
st.sidebar.divider()
st.sidebar.page_link('pages/5_ponto_de_equilibrio.py', label='Ponto de Equilíbrio', icon='⚖️')


def calcula_markup(perc_mrg_liq, perc_despesas, perc_custos):    
    markup = 1.0/(1.0 - perc_mrg_liq - perc_despesas - perc_custos)
    #custos_produtos = faturamento / markup
    st.session_state.markup = markup
    #st.session_state.custos_produtos = custos_produtos
    return markup

    
def painel_markup():
    st.write('<h2>Markup</h2>', unsafe_allow_html=True)
    st.info("""
                Use o indicador abaixo para precificar os seus produtos.\n 
                Basta multiplicar o preço de custo (o mesmo da nota fiscal) pelo markup e terá o preço de venda ideal.
                """)

    
    # 1 faturamento
    faturamento = st.session_state.dados_faturamento['faturamento']
    perc_mrg_liq = st.session_state.dados_faturamento['%_margem'] / 100.0
    mrg_liq = st.session_state.dados_faturamento['margem_liq']

    # 2 despesas
    perc_despesas= st.session_state.despesas_fixas['%_despesas_fixas'] / 100.0
    despesas= st.session_state.despesas_fixas['total_despesas_fixas']

    # 3 custos
    perc_custos= st.session_state.custos_variaveis['%_custos_variaveis'] / 100.0
    custos= st.session_state.custos_variaveis['total_custos_variaveis']
        

    markup = calcula_markup(perc_mrg_liq, perc_despesas, perc_custos)
    custos_produtos = faturamento / markup
    st.session_state.custos_produtos = custos_produtos
    
    mrg_ctb = faturamento - custos - custos_produtos
    perc_mrg_ctb = mrg_ctb / faturamento
    st.session_state.mrg_ctg = mrg_ctb
    st.session_state.perc_mrg_ctg = perc_mrg_ctb * 100.0

        
    st.write(f'<p class="markup"> {round(markup,2)}</p>', unsafe_allow_html=True)

    st.success('Prossiga para a última página clicando em - ⚖️Ponto de Equilibrio - na barra lateral')


#st.sidebar.write(f'registros da sessão :',st.session_state)




        
painel_markup()