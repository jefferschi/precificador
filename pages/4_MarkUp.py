import streamlit as st

import pandas as pd
import plotly.express as px

#import locale

#locale.setlocale(locale.LC_ALL, 'pt_BR')

with open('estilo.css') as estilo:
    st.markdown(f'<style>{estilo.read()}</style>', unsafe_allow_html=True)

def calcula_markup(perc_mrg_liq, perc_despesas, perc_custos,faturamento):
    markup = 1.0/(1.0-perc_mrg_liq - perc_despesas - perc_custos)
    custos_produtos = faturamento / markup
    st.session_state.markup = markup
    st.session_state.custos_produtos = custos_produtos

    
def painel_markup():
    st.subheader("Markup")
    
    faturamento = st.session_state.dados_faturamento['faturamento']
    perc_mrg_liq = st.session_state.dados_faturamento['%_margem']
    perc_despesas= st.session_state.despesas_fixas['%_despesas_fixas']
    perc_custos= st.session_state.custos_variaveis['%_custos_variaveis']

    mrg_liq = st.session_state.dados_faturamento['margem_liq']
    despesas= st.session_state.despesas_fixas['total_despesas_fixas']
    custos= st.session_state.custos_variaveis['total_custos_variaveis']

    custos_produtos = st.session_state.get('custos_produtos',0.0)

    
    col1, col2, col3, col4 = st.columns([1,1,1,0.5])
    with col1:
        st.write('Faturamento e Margem Líquida')
        st.write('Faturamento estimado: ', faturamento)
        st.write('Margem líquida estimada: ', mrg_liq)
        st.write('% margem líquida: ', perc_mrg_liq)


    with col2:
        st.write('Despesas Fixas')
        st.write('Total das despesas fixas: ', despesas)
        st.write('% das despesas fixas: ', perc_despesas)


    with col3:
        st.write('Custos Variáveis')
        st.write('Total dos custos variávies: ', custos)
        st.write('% custos variáveis: ', perc_custos)

    with col4:
        st.write('Markup')
        calcula_markup(perc_mrg_liq, perc_despesas, perc_custos, faturamento)
        st.write(st.session_state.markup)
    
    grafico(mrg_liq, despesas, custos,custos_produtos)

st.sidebar.write(f'registros da sessão :',st.session_state)


def grafico(mrg_liq, despesas, custos, custos_produtos):

    rotulos = ['Margem Líquida','Despesas Fixas', 'Custos Variáveis','Custos Produtos']

    valores = [ mrg_liq, despesas, custos, custos_produtos]

    pizza = px.pie(values=valores, names=rotulos)

    st.plotly_chart(pizza)

        
painel_markup()