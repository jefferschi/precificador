import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Despesas Fixas",
    page_icon='💸',
)

st.sidebar.page_link('Home.py', label='Home', icon='🏠')
st.sidebar.page_link('pages/1_faturamento.py', label='Faturamento', icon='💲')
st.sidebar.divider()

@st.cache_data
def processar_dados(despesas_fixas):
    df_despesas_fixas = pd.DataFrame(despesas_fixas, index=[0])
    return df_despesas_fixas

# Calculando o total e armazenando na sessão
def soma_despesas(despesas_fixas):
    faturamento = st.session_state.dados_faturamento.get('faturamento',0.0)
    st.session_state.despesas_fixas['total_despesas_fixas'] = 0.0
    st.session_state.despesas_fixas['%_despesas_fixas'] = 0.0

    # soma as despesas
    total = 0.0
    total = sum(despesas_fixas.values())
    st.session_state.despesas_fixas['total_despesas_fixas'] = total
    
    # encontra o percentual das despesas sobre o faturamento
    perc_despesas_fixas = 0.0
    perc_despesas_fixas = total / faturamento
    st.session_state.despesas_fixas['%_despesas_fixas'] = perc_despesas_fixas * 100.0
    

def formulario_despesas_fixas():    
    st.subheader("Despesas Fixas")    

    # Recuperando os despesas_fixas dos inputs usando st.session_state
    despesas_fixas = st.session_state.get('despesas_fixas', {
        'funcionarios': 0.0,
        'aluguel': 0.0,
        'luz_agua_internet_telefone': 0.0,
        'contador': 0.0,
        'pro_labore': 0.0,
        'outros': 0.0            
    })

    with st.form(key='formulario_despesas_fixas'):
        

        #'%_despesas_fixas':0.0,
        #'total_despesas_fixas':0.0
        
        # Campos para despesas fixas
        despesas_fixas['funcionarios'] = st.number_input("Funcionários", step=100.0, value=despesas_fixas['funcionarios'], min_value=0.0, key="funcionarios")
        despesas_fixas['aluguel'] = st.number_input("Aluguel", step=100.0, value=despesas_fixas['aluguel'], min_value=0.0, key="aluguel")
        despesas_fixas['luz_agua_internet_telefone'] = st.number_input("Luz + Água + Internet + Telefone", step=100.0, value=despesas_fixas['luz_agua_internet_telefone'], min_value=0.0, key="luz_agua_internet_telefone")
        despesas_fixas['contador'] = st.number_input("Contador", step=100.0, value=despesas_fixas['contador'], min_value=0.0, key="contador")
        despesas_fixas['pro_labore'] = st.number_input("Pró-labore", step=1000.0, value=despesas_fixas['pro_labore'], min_value=0.0, key="pro_labore")
        despesas_fixas['outros'] = st.number_input("Outros", step=100.0, value=despesas_fixas['outros'], min_value=0.0, key="outros")

        # Salvando os despesas_fixas dos inputs na sessão usando st.session_state
        st.session_state['despesas_fixas'] = despesas_fixas
        
        # chamando função para somar despesas
        soma_despesas(despesas_fixas)

        # atualizando a barra lateral com despesas_fixas da sessão    
        #st.sidebar.write(f'registros da sessão :',st.session_state)

        # botão para enviar o formulário
        botao_salvar = st.form_submit_button(label='Salvar')

    if botao_salvar:
        # verificar por que precisa apertar duas vezes salvar para imputar os dados na sessão
        dados = processar_dados(despesas_fixas)
        #st.write(dados)

        if st.session_state.despesas_fixas['total_despesas_fixas'] > 0.0:
            st.sidebar.page_link('pages/3_custos_variaveis.py', label='Custos Variáveis', icon='➗')
            st.success('Prossiga para a próxima página clicando em - ➗Custos Variáveis - na barra lateral')
    
formulario_despesas_fixas()


