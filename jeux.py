#importation des bibliothèques et des supports
import streamlit as st
from pendu import * 
from gagne_perd import *
import time
import random


#création de la fonction pour le pile ou face 
def jeux():
    if "choix" not in st.session_state:
        st.session_state["choix"]=None #on crée une variable NoType dans laquelle on stockera le choix de l'utilisateur
    if "anime" not in st.session_state:
        st.session_state["anime"]=False #on crée une variable booléenne qui sert à afficher l'animation 
    
    st.title("Pile ou face") #mise en page du titre 
    
    
    #création des colonnes 
    col1,col2=st.columns(2)
    with col2: 
        b=st.container(height=200) #on crée une case de taille 200 
        with b:
            if st.session_state["anime"]==True:
                st.image("https://www.icone-gif.com/gif/pieces-de-monnaie/divers/piece-gif-009.gif") #s'il faut mettre l'animation alors afficher l'animation

            elif st.session_state["choix"]!=None:
                piece=random.choice(["pile","face"]) #création de du choix aléatoire
                if piece==st.session_state["choix"]:
                    st.write("Gagné !") #si la pièce qu'a choisis le joueur est pareille que celle choisis au hasard alors on affiche gagné 
                    gagne() #appelle de la fonction gagne qui ajoute de l'humeur au tamagotchi et affiche des ballons 
                else:
                    st.write("Perdu...")#si la pièce qu'a choisis le joueur n'est pas la même que celle choisis au hasard alors on affiche perdu
                    perd() #appelle de la fonction perd qui ajoute de l'humeur au tamagotchi
    
    with col1:
        a=st.container(height=200) #on crée une case de taille 200
        with a:
            if st.session_state["choix"]==None:
                if st.button("PILE"): #si bouton pile est choisis
                    time.sleep(0.2) #temps d'attente pour éviter les bugs 
                    st.session_state["choix"]="pile" #on donne à la variable choix la valeur pile
                    st.session_state["anime"]=True #on débloque l'animation
                    st.rerun()
                if st.button("FACE"): #si bouton face est choisis
                    time.sleep(0.2) #temps d'attente pour éviter les bugs
                    st.session_state["choix"]="face" #on donne à la variable choix la valeur face
                    st.session_state["anime"]=True  #on débloque l'animation
                    st.rerun()
            else:
                st.write(f"Votre choix: {st.session_state['choix']}")
                if st.session_state["anime"]==False: 
                    if st.button('Rejouer'): #faire un bouton rejouer
                        st.session_state["choix"]=None #on attribue rien à la variable choix 
                        st.session_state["anime"]=False #on bloque l'animation
                        st.rerun()
            if st.session_state["anime"]==True:
                time.sleep(2.5)
                st.session_state["anime"]=False
                st.rerun()
    
    if st.button("Retour au mode 'jeux'"):  #bouton pour revenir à la page normale 
        st.session_state["choix"]=None
        st.session_state["anime"]=False
        st.session_state['situation']='jeux' #retour de à la page normale si le bouton est cliqué
        st.rerun()