import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Faturamento",
    page_icon='💲',
      
)

# arquivo css
with open('estilo.css') as estilo:
    st.markdown(f'<style>{estilo.read()}</style>', unsafe_allow_html=True)


st.sidebar.page_link('Home.py', label='Home', icon='🏠')
st.sidebar.divider()


@st.cache_data
def processar_dados(dados_faturamento):
    df_dados_faturamento = pd.DataFrame(dados_faturamento, index=[0])
    return df_dados_faturamento

def calcula_margem(dados_faturamento):
    margem_liq = dados_faturamento['faturamento'] * (dados_faturamento['%_margem'] / 100.0)
    st.session_state.dados_faturamento['margem_liq'] = margem_liq
    
    #st.session_state.margem_liq = margem_liq


def formulario_faturamento():

    with st.expander(label='Saiba como preencher os campos',expanded=False):
        st.markdown("""
                    <p class="expandido">* Faturamento: a média mensal das vendas. (retire os meses excepcionais, quando houver) <br>
                    * % Margem Líq. desejada: a expectativa de lucro sobre o faturamento em percentual.
                    </p>
                    """, unsafe_allow_html=True
                    )

    st.subheader("Faturamento Mensal")

    # Recuperando o valor do input usando st.session_state e inicializando caso não exista    
    #faturamento = st.session_state.get('faturamento', 0.0)        
    dados_faturamento = st.session_state.get('dados_faturamento',{
        'faturamento':0.0,
        '%_margem':0.0,
        'margem_liq':0.0,
        })

    with st.form(key='formulario_faturamento'):
        #fat ="{:,.2f}".format(dados_faturamento['faturamento'])
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
        #st.dataframe(dados)
        #st.write('Margem Líquida: ',st.session_state.dados_faturamento['margem_liq'])
        
        if st.session_state.dados_faturamento['margem_liq'] > 0.0:
            st.sidebar.page_link('pages/2_despesas_fixas.py', label='Despesas Fixas', icon='💸')
            st.success('Prossiga para a próxima página clicando em - 💸Despesas Fixas - na barra lateral')



    


formulario_faturamento()

# impressões na tela
    #st.write(f'variavel faturamento após input',dados_faturamento)
    #st.write(f'Faturamento: ',st.session_state['faturamento'])

    #st.sidebar.write('faturamento: %.2f'%st.session_state.faturamento)
    #st.sidebar.write('faturamento: %.2f'%st.session_state.dados_faturamento['faturamento'])