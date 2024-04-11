import streamlit as st
import pandas as pd


#import locale

# colocar um campo para %margem líq e retornar o cálculo nominal. colocar um st.form

#locale.setlocale(locale.LC_ALL, 'pt_BR')

st.sidebar.page_link('Home.py', label='Home', icon='🏠')


@st.cache_data
def processar_dados(dados_faturamento):
    df_dados_faturamento = pd.DataFrame(dados_faturamento, index=[0])
    return df_dados_faturamento

def calcula_margem(dados_faturamento):
    margem_liq = dados_faturamento['faturamento'] * dados_faturamento['%_margem']
    st.session_state.dados_faturamento['margem_liq'] = margem_liq
    
    #st.session_state.margem_liq = margem_liq

def formulario_faturamento():

    st.subheader("Faturamento Mensal")

    # Recuperando o valor do input usando st.session_state e inicializando caso não exista    
    #faturamento = st.session_state.get('faturamento', 0.0)        
    dados_faturamento = st.session_state.get('dados_faturamento',{
        'faturamento':0.0,
        '%_margem':0.0,
        'margem_liq':0.0,
        })

    with st.form(key='formulario_faturamento'):
        
        # entrada do valor de faturamento
        dados_faturamento['faturamento'] = st.number_input("Faturamento", step=1000.0, value=dados_faturamento['faturamento'], min_value=0.0, key='faturamento')        
        dados_faturamento['%_margem'] = st.number_input("% Margem Líq. desejada", value=dados_faturamento['%_margem'], min_value=0.0, key='%_margem')
        
        
        # Salvando o valor do input na sessão usando st.session_state
        st.session_state['dados_faturamento'] = dados_faturamento
        
        # calcula margem
        calcula_margem(dados_faturamento)

        #st.sidebar.write(f'registros da sessão :',st.session_state)
        
        botao_salvar = st.form_submit_button(label='Salvar')

    if botao_salvar:
        dados = processar_dados(dados_faturamento)
        st.write(dados)
        st.write('Margem Líquida: ',st.session_state.dados_faturamento['margem_liq'])
    
        
        if st.session_state.dados_faturamento['margem_liq'] > 0.0:
            st.sidebar.page_link('pages/despesas_fixas.py', label='Despesas Fixas', icon='💸')


    


formulario_faturamento()

# impressões na tela
    #st.write(f'variavel faturamento após input',dados_faturamento)
    #st.write(f'Faturamento: ',st.session_state['faturamento'])

    #st.sidebar.write('faturamento: %.2f'%st.session_state.faturamento)
    #st.sidebar.write('faturamento: %.2f'%st.session_state.dados_faturamento['faturamento'])