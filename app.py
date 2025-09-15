import streamlit as st
import pandas as pd

st.sidebar.image("logo.png")
st.sidebar.title('Maria Playlist')

generos = ["Pop", "Sertanejo", "Funk"]

artistas_por_genero = {"Pop": ["Justin Bieber", "Taylor Swift", "Shawn Mendes"],
                       "Sertanejo": ["Henrique e Juliano", "Marília Mendonça", "Jorge e Mateus"],
                       "Funk": ["MC Hariel", "Anitta", "MC Livinho"]}


genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)


if genero_selecionado:
    artista_selecionado = st.sidebar.selectbox("Selecione o Artista:", artistas_por_genero[genero_selecionado])



if genero_selecionado and artista_selecionado:

    st.title('Maria Playlist')

    st.markdown(f'## Você escolheu o Gênero: {genero_selecionado}')
    st.markdown(f'## Artista: {artista_selecionado}')
    st.image(f'{artista_selecionado}.png')

    st.markdown('---')

if genero_selecionado == 'Pop' and artista_selecionado == 'Justin Bieber':
     st.write('Justin Bieber é um cantor canadense que ganhou fama mundial ainda jovem, destacando-se no pop contemporâneo com vários sucessos globais.')
     st.video('https://www.youtube.com/watch?v=CHVhwcOg6y8&pp=ygUNanVzdGluIGJpZWJlcg%3D%3D')

elif genero_selecionado == 'Pop' and artista_selecionado == 'Taylor Swift':
    st.write('Taylor Swift é uma cantora e compositora americana, reconhecida mundialmente por suas músicas nos gêneros country e pop, com uma carreira marcada por grandes sucessos e prêmios.')
    st.video('https://www.youtube.com/watch?v=-CmadmM5cOk&list=RD-CmadmM5cOk&start_radio=1&pp=ygUMdGF5bG9yIHN3aWZ0oAcB')

elif genero_selecionado == 'Pop' and artista_selecionado == 'Shawn Mendes':
    st.write('Shawn Mendes é um cantor e compositor canadense, conhecido por seu pop contemporâneo e sucesso global, consolidado desde sua descoberta nas redes sociais.')
    st.video('https://www.youtube.com/watch?v=dT2owtxkU8k&list=RDdT2owtxkU8k&start_radio=1&pp=ygUdc2hhd24gbWVuZGVzIHRyZWF0IHlvdSBiZXR0ZXKgBwE%3D')

elif genero_selecionado == 'Sertanejo' and artista_selecionado == 'Henrique e Juliano':
    st.write('Henrique e Juliano são uma dupla brasileira de sertanejo, reconhecida por sucessos comerciais e impacto relevante no cenário musical nacional.')
    st.video('https://www.youtube.com/watch?v=pQuiUCRtvus&pp=ygUlaGVucmlxdWUgZSBqdWxpYW5vIGF0ZSBhIHByb3hpbWEgdmlkYQ%3D%3D')

elif genero_selecionado == 'Sertanejo' and artista_selecionado == 'Marília Mendonça':
    st.write('Marília Mendonça foi uma cantora e compositora brasileira, referência no sertanejo universitário, conhecida por suas letras emotivas e grande influência na música brasileira até seu falecimento em 2021.')
    st.video('https://www.youtube.com/watch?v=2nH7xAMqD2g&list=RD2nH7xAMqD2g&start_radio=1&pp=ygURbWFyaWxpYSBtZW5kb27Dp2GgBwE%3D')

elif genero_selecionado == 'Sertanejo' and artista_selecionado == 'Jorge e Mateus':
    st.write('Jorge e Mateus são uma dupla brasileira de sertanejo, reconhecida por grandes sucessos e por serem uma das principais referências do gênero no Brasil.')
    st.video('https://www.youtube.com/watch?v=7INcDQlK-7g&list=RD7INcDQlK-7g&start_radio=1&pp=ygUcam9yZ2UgZSBtYXRldXMgcGVyZ3VudGEgYm9iYaAHAQ%3D%3D')

elif genero_selecionado == 'Funk' and artista_selecionado == 'MC Hariel':
    st.write('MC Hariel é um cantor e compositor brasileiro, destaque no cenário do funk paulista, conhecido por suas letras que retratam a realidade urbana com autenticidade e sucesso crescente na música popular.')
    st.video('https://www.youtube.com/watch?v=tUJXtHMXDY0&pp=ygUVbWMgaGFyaWVsIG1hw6dhIHZlcmRl')

elif genero_selecionado == 'Funk' and artista_selecionado == 'Anitta':
    st.write('Anitta é uma cantora, compositora e empresária brasileira, reconhecida internacionalmente por seu trabalho no pop e funk carioca, além de ser uma das artistas brasileiras de maior destaque no mercado global.')
    st.video('https://www.youtube.com/watch?v=SmpNmsuNA2E&list=RDSmpNmsuNA2E&start_radio=1&pp=ygUGYW5pdHRhoAcB')

elif genero_selecionado == 'Funk' and artista_selecionado == 'MC Livinho':
    st.write('MC Livinho é um cantor e compositor brasileiro, destaque no funk paulista, conhecido por suas músicas que combinam batidas envolventes com letras românticas e de festa, conquistando grande popularidade nacional.')
    st.video('https://www.youtube.com/watch?v=cplbrMIL2Rk&list=RDcplbrMIL2Rk&start_radio=1&pp=ygUYbWMgbGl2aW5obyBhenVsIHBpc2NpbmFzoAcB')

