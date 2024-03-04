import streamlit as st

def perd(): #création de la fonction perd() qui augmente l'humeur du tamagotchi
    if st.session_state['humeur'] <=8: #si l'humeur est < ou = à 8, ajouter 2
        st.session_state['humeur'] += 2
    elif st.session_state['humeur'] ==9: #sinon si l'humeur est de 9, ajouter 1 (pour ne pas dépasser 10)
        st.session_state['humeur'] += 1

def gagne(): #création de la fonction perd() qui augmente l'humeur du tamagotchi
    st.balloons()
    if st.session_state['humeur'] <=6: #si l'humeur est < ou = à 6, ajouter 4
        st.session_state['humeur'] += 4
    elif st.session_state['humeur'] <10: #sinon si l'humeur est >6 et <10, mettre humeur à 10 (pour ne pas dépasser)
        st.session_state['humeur'] =10