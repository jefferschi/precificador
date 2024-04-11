import streamlit as st

import pandas as pd
import plotly.express as px

st.sidebar.page_link('Home.py', label='Home', icon='🏠')
st.sidebar.page_link('pages/3_custos_variaveis.py', label='Custos Variáveis', icon='➗')
st.sidebar.page_link('pages/5_ponto_de_equilibrio.py', label='Ponto de Equilíbrio', icon='⚖️')



with open('estilo.css') as estilo:
    st.markdown(f'<style>{estilo.read()}</style>', unsafe_allow_html=True)

def calcula_markup(perc_mrg_liq, perc_despesas, perc_custos,faturamento):
    
    markup = 1.0/(1.0 - perc_mrg_liq - perc_despesas - perc_custos)
    #custos_produtos = faturamento / markup
    st.session_state.markup = markup
    #st.session_state.custos_produtos = custos_produtos
    return markup

    
def painel_markup():
    st.subheader("Markup")
    
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

    #custos_produtos = st.session_state.get('custos_produtos',0.0)
    #st.write(st.session_state.custos_produtos)

    #mrg_ctb = faturamento - custos - custos_produtos
    #perc_mrg_ctb = mrg_ctb / faturamento
    #st.session_state.mrg_ctg = mrg_ctb
    #st.session_state.perc_mrg_ctg = perc_mrg_ctb * 100.0

    
    col1, col2, col3, col4 = st.columns([1,1,1,0.5])
    with col1:
        st.write('Faturamento e Margem Líquida')
        st.write('Faturamento estimado: ', faturamento)
        st.write('Margem líquida estimada: ', mrg_liq)
        st.write('% margem líquida: ', perc_mrg_liq * 100.0)


    with col2:
        st.write('Despesas Fixas')
        st.write('Total das despesas fixas: ', despesas)
        st.write('% das despesas fixas: ', perc_despesas * 100.0)


    with col3:
        st.write('Custos Variáveis')
        st.write('Total dos custos variávies: ', custos)
        st.write('% custos variáveis: ', perc_custos * 100.0)

    with col4:
        st.write('Markup')
        markup = calcula_markup(perc_mrg_liq, perc_despesas, perc_custos, faturamento)
        custos_produtos = faturamento / markup
        st.session_state.custos_produtos = custos_produtos
        
        mrg_ctb = faturamento - custos - custos_produtos
        perc_mrg_ctb = mrg_ctb / faturamento
        st.session_state.mrg_ctg = mrg_ctb
        st.session_state.perc_mrg_ctg = perc_mrg_ctb * 100.0

        st.write(st.session_state.markup)
        st.write('% Margem de Contribuição \n', st.session_state.perc_mrg_ctg)

    
    grafico(mrg_liq, despesas, custos, custos_produtos)

    st.success('Prossiga para a próxima última página clicando em - ⚖️Ponto de Equilibrio - na barra lateral')


#st.sidebar.write(f'registros da sessão :',st.session_state)


def grafico(mrg_liq, despesas, custos, custos_produtos):

    rotulos = ['Margem Líquida','Despesas Fixas', 'Custos Variáveis','Custos Produtos']

    valores = [ mrg_liq, despesas, custos, custos_produtos]

    pizza = px.pie(values=valores, names=rotulos)

    st.plotly_chart(pizza)

        
painel_markup()