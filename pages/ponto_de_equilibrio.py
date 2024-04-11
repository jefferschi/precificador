import streamlit as st

import pandas as pd

st.sidebar.page_link('Home.py', label='Home', icon='🏠')
st.sidebar.page_link('pages/markup.py', label='Markup', icon='🏷️')


def ponto_equilibrio_fin():
    ponto_equilibrio_fin = st.session_state.get('ponto_eq_fin',0.0)

    faturamento = st.session_state.dados_faturamento['faturamento']
    despesas= st.session_state.despesas_fixas['total_despesas_fixas']
    custos= st.session_state.custos_variaveis['total_custos_variaveis']
    custos_produtos = st.session_state.custos_produtos
    
    mrg_ctb = faturamento - custos - custos_produtos
    perc_mrg_ctb = mrg_ctb / faturamento
    st.session_state.mrg_ctg = mrg_ctb
    st.session_state.perc_mrg_ctg = perc_mrg_ctb
    
  
    # testar aqui fórmulas para se chegar ao valor mais assertivo de P.E.
    ponto_equilibrio_fin = custos + custos_produtos + despesas
    #ponto_equilibrio_fin2 = despesas / perc_mrg_ctb

    st.session_state.ponto_equilibrio_fin = ponto_equilibrio_fin
    st.write(ponto_equilibrio_fin)
    #st.write(ponto_equilibrio_fin2)


def ponto_equilibrio_eco():
    ponto_equilibrio_eco = st.session_state.get('ponto_equilibrio_eco',0.0)
    ponto_equilibrio_fin = st.session_state.get('ponto_equilibrio_fin',0.0)
    mrg_liq = st.session_state.dados_faturamento['margem_liq']

    ponto_equilibrio_eco = ponto_equilibrio_fin + mrg_liq

    st.session_state.ponto_equilibrio_eco = ponto_equilibrio_eco
    st.write(ponto_equilibrio_eco)


def painel_ponto_equilibrio():
    st.header('Ponto de Equilíbrio')
    #st.subheader('Ponto de Equilíbrio Financeiro')
    ponto_equilibrio_fin()
    st.write('% Margem de Contribuição', st.session_state.perc_mrg_ctg)

    
    #st.subheader('Ponto de Equilíbrio Econômico')
    #ponto_equilibrio_eco()

painel_ponto_equilibrio()
    