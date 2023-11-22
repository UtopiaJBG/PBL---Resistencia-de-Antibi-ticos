import pandas as pd
import streamlit as st
from PIL import Image

# Header e Subheader - fazem o título e o subtítulo
st.header("Painel de Monitoramento de Antibióticos")
st.subheader('Dados Interativos de antibióticos no período de 2017-2023', divider='rainbow')

# carregando imagem para o logo
img = Image.open("imagem-logo.png")

# dividindo o espaçamento da tela em colunas
left_col, cent_col, last_col, center_left, right_col = st.columns(5) 

# colocando o logo na coluna central
with cent_col:
    st.image(img, width=500)

# Texto introdutório

st.markdown("Projeto engenharia biomédica - Grupo 3")



