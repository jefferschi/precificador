
# ver como usar para personalizar a aplicação

import streamlit as st
import streamlit.components.v1 as components

import locale
"""
# informações na barra lateral de totais    
    
media_faturamento = st.session_state.total_faturamento
media_faturamento_s = locale.format_string("%.2f",media_faturamento,grouping=True)
st.sidebar.write("Faturamento Mensal: ",media_faturamento_s)
#st.sidebar.write(f"Faturamento Mensal: {media_faturamento_s}")

total_despesas = st.session_state.total_despesas
total_despesas_s = locale.format_string("%.2f",total_despesas,grouping=True)
st.sidebar.write("Total de Despesas Fixas: ",total_despesas_s)
#st.sidebar.write(f"Total de Despesas Fixas: {total_despesas_s}")
#exemplo retirado de despesas fixas
total_custos = st.session_state.total_custos
total_custos_s = locale.format_string("%.2f",total_custos,grouping=True)
st.sidebar.write("Total de Custos Variáveis: ",total_custos_s)

"""
# bootstrap 4 collapse example

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)
