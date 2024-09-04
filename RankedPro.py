import streamlit as st
import pandas as pd
import ranking as rk

#------|CONFIG|----------#
# if __name__ == "__main__":
#     import os
#     port = int(os.environ.get("PORT", 8501))
#     st.run("RankedPro.py", server_port=port)

#--------| TOPO | --------#
head = st.container()
h1,h2,h3 = st.columns(3)

#--------| MEIO | --------#
body = st.container()
a1,a2,a3,a4 = st.columns(4)

st.set_page_config(page_title='RankedPro')

with head:
    with h2:
        logo = st.image('ranked-white.png')



with body:
    with a1:
        pi = int(st.number_input('Pontos Iniciais',key='pi'))
    with a2:
        pf = int(st.number_input('Pontos Atuais',key='pf'))
    with a3:
        res = pf - pi
        rank,logo = rk.rank(pf)
        stats = st.metric(label='Ranking Atual',value=f'{rank}',delta=f'{res}')
    with a4:
        st.image(f'{logo}')