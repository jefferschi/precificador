import streamlit as st

import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Ponto de Equilíbrio",
    page_icon='⚖️',
)

with open('estilo.css') as estilo:
    st.markdown(f'<style>{estilo.read()}</style>', unsafe_allow_html=True)


st.sidebar.page_link('Home.py', label='Home', icon='🏠')
st.sidebar.page_link('pages/4_markup.py', label='Markup', icon='🏷️')


def ponto_equilibrio_fin():
    ponto_equilibrio_fin = st.session_state.get('ponto_eq_fin',0.0)

    faturamento = st.session_state.dados_faturamento['faturamento']
    despesas= st.session_state.despesas_fixas['total_despesas_fixas']
    custos= st.session_state.custos_variaveis['total_custos_variaveis']
    custos_produtos = st.session_state.custos_produtos
    
    # testar aqui fórmulas para se chegar ao valor mais assertivo de P.E.
    ponto_equilibrio_fin = custos + custos_produtos + despesas
    #ponto_equilibrio_fin2 = despesas / perc_mrg_ctb

    st.session_state.ponto_equilibrio_fin = ponto_equilibrio_fin

    return ponto_equilibrio_fin


def ponto_equilibrio_eco():
    ponto_equilibrio_eco = st.session_state.get('ponto_equilibrio_eco',0.0)
    ponto_equilibrio_fin = st.session_state.get('ponto_equilibrio_fin',0.0)
    mrg_liq = st.session_state.dados_faturamento['margem_liq']

    ponto_equilibrio_eco = ponto_equilibrio_fin + mrg_liq

    st.session_state.ponto_equilibrio_eco = ponto_equilibrio_eco
    st.write(ponto_equilibrio_eco)


def painel_ponto_equilibrio():
    st.header('Ponto de Equilíbrio')
    st.info("""
            Este é o valor necessário a faturar para pagar todas as despesas da empresa e fechar o mês no 0 x 0.\n
            Ou seja, não há lucro e nem prejuízo.\n
            """)
    st.warning('Atenção!!! Esta projeção é baseada nas informações inseridas pelo gestor nesta aplicação.')
    
    ponto_eq = ponto_equilibrio_fin()
    ponto_eq_formatado = "R$ {:,.0f}".format(ponto_eq).replace(',','.')
    st.write(f'<p class="ponto-equilibrio">{ponto_eq_formatado}</p>',unsafe_allow_html=True)
    
    st.write('-'*1000)
    st.write('Resumo')

    mrg_liq = st.session_state.dados_faturamento['margem_liq']
    faturamento = st.session_state.dados_faturamento['faturamento']

    despesas= st.session_state.despesas_fixas['total_despesas_fixas']
    custos= st.session_state.custos_variaveis['total_custos_variaveis']

    markup = st.session_state.markup
    custos_produtos = faturamento / markup

    grafico(mrg_liq, despesas, custos, custos_produtos)
    
def grafico(mrg_liq, despesas, custos, custos_produtos):

    rotulos = ['Margem Líquida','Despesas Fixas', 'Custos Variáveis','Custos Produtos']

    valores = [ mrg_liq, despesas, custos, custos_produtos]

    pizza = px.pie(values=valores, names=rotulos)

    st.plotly_chart(pizza)

painel_ponto_equilibrio()
    