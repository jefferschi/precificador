import streamlit as st

import pandas as pd
#import locale

#locale.setlocale(locale.LC_ALL, 'pt_BR')

@st.cache_data
def processar_dados(custos_variaveis):
    df_custos_variaveis = pd.DataFrame(custos_variaveis, index=[0])
    return df_custos_variaveis

def calcula_custos_variaveis(perc_comissao, perc_impostos, perc_cartao_s_fat, perc_taxa_cartao, perc_outros):

    faturamento = st.session_state.dados_faturamento.get('faturamento',0.0)

    ### lembrar de tratar os arredondamentos para evitar os erros próprios das máquinas de cálculo float 
    comissao = perc_comissao * faturamento
    st.session_state.custos_variaveis['comissao'] = comissao

    impostos = perc_impostos * faturamento
    st.session_state.custos_variaveis['impostos'] = impostos
    
    taxa_cartao = (perc_cartao_s_fat * faturamento) * perc_taxa_cartao
    st.session_state.custos_variaveis['taxa_cartao'] = taxa_cartao

    outros = perc_outros * faturamento
    st.session_state.custos_variaveis['outros'] = outros

    total_custos_variaveis = comissao + impostos + taxa_cartao + outros
    st.session_state.custos_variaveis['total_custos_variaveis'] = total_custos_variaveis
    
    perc_custos_variaveis = total_custos_variaveis / faturamento
    st.session_state.custos_variaveis['%_custos_variaveis'] = perc_custos_variaveis
    

def formulario_custos_variaveis():
    st.subheader("Custos Variáveis")

    with st.form(key='formulario_custos_variaveis'):
    
        # Recuperando os valores dos inputs usando st.session_state
        custos_variaveis = st.session_state.get('custos_variaveis', {
            "%_comissao": 0.0,
            "comissao": 0.0,
            '%_impostos': 0.0,
            'impostos': 0.0,
            '%_cartao_sobre_faturamento': 0.0,            
            '%_taxa_cartao': 0.0,
            'taxa_cartao': 0.0,
            '%_outros': 0.0,
            'outros': 0.0            
        })
        #'%_custos_variaveis':0.0,
        #'total_custos_variaveis':0.0
             
        # entrada dos percentuais de custos
        custos_variaveis['%_comissao'] = st.number_input('comissão %', step=0.01, value=custos_variaveis['%_comissao'], min_value=0.0, key='%_comissao')
        custos_variaveis['%_impostos'] = st.number_input('impostos %', step=0.01, value=custos_variaveis['%_impostos'], min_value=0.0, key='%_impostos')
        custos_variaveis['%_cartao_sobre_faturamento'] = st.number_input('cartão sobre o faturamento %', step=0.01, value=custos_variaveis['%_cartao_sobre_faturamento'], min_value=0.0, key='%_cartao_sobre_faturamento')
        custos_variaveis['%_taxa_cartao'] = st.number_input('taxa do cartão %', step=0.01, value=custos_variaveis['%_taxa_cartao'], min_value=0.0, key='%_taxa_cartao')
        custos_variaveis['%_outros'] = st.number_input('outros %', step=0.01, value=custos_variaveis['%_outros'], min_value=0.0, key='%_outros')

        # Salvando o valor do input na sessão usando st.session_state
        st.session_state['custos_variaveis'] = custos_variaveis

        calcula_custos_variaveis(custos_variaveis['%_comissao'],custos_variaveis['%_impostos'],
                                 custos_variaveis['%_cartao_sobre_faturamento'],
                                 custos_variaveis['%_taxa_cartao'],
                                 custos_variaveis['%_outros']
                                 )
        
        st.sidebar.write(f'registros da sessão :',st.session_state)

        botao_salvar = st.form_submit_button(label='Salvar')
    
    if botao_salvar:        
        
        dados = processar_dados(custos_variaveis)
        st.write(dados)     
        st.write('Valor comissão: ',st.session_state.custos_variaveis['comissao'])

        
formulario_custos_variaveis()