import streamlit as st
import random
import time
from gagne_perd import *

def memoire():
    col1, col2=st.columns(2) #séparation de l'écran en 2
    couleurs=[":red", ":orange", ":green", ":blue", ":violet", ":gray", ":rainbow"] #création d'une liste comprenant tous les codes nécessaires pour changer la couleur de textes
    mots=["énigme","mémoire","chocolat","mesure","outils","encre","joue","beurre","koala","souris"] #création d'une liste de mots
    mots_2=["violet","vert","rose","orange","bleu","noir","jaune","rouge","gris"]
    
    #initialisation des variables de session
    if 'sol' not in st.session_state or st.session_state['sol']==None:
        st.session_state['sol']=[] #création d'une liste vide dans laquelle on mettra la solution du jeu
        for i in range(5):  #(5 fois)
            k=f"{random.choice(couleurs)}[{random.choice(mots)}]"  #on prend un mot au hasard (liste mots) et on l'affiche d'une couleur au hasard (liste couleurs)
            if k not in st.session_state['sol']:  #si cette combinaison n'y est pas déjà, l'ajouter à la solution
                st.session_state['sol'].append(k)

    if 'prop' not in st.session_state or st.session_state['prop']==None:
        st.session_state['prop']=[]   #création d'une liste vide dans laquelle on mettra les propositions faites au joueur
        for i in st.session_state['sol']:  #faire défiler la liste contenant les mots de la solution
            st.session_state['prop'].append(i)  #ajouter ces mots à la variables contenant les propositions
        for i in range(5):  #(5 fois)
            h=f"{random.choice(couleurs)}[{random.choice(mots)}]"  #on prend un mot au hasard (liste mots) et on l'affiche d'une couleur au hasard (liste couleurs)
            if h not in st.session_state['prop']: #si la combinaison n'est pas déjà dans les propositions, l'ajouter à la liste de propositions (pour éviter les bugs dus aux répétitions de mêmes boutons)
                st.session_state['prop'].append(h)
        random.shuffle(st.session_state['prop'])   #mélanger la liste de propositions
    if 'rep' not in st.session_state or st.session_state['rep']==None:
        st.session_state['rep']=[]   #création d'une liste vide dans laquelle on mettra la réponse donnée par le joueur
    if 'resultat' not in st.session_state:
        st.session_state['resultat']=None  #création d'une variable NoType qui contiendra le résultat du jeu
    if 'montrer' not in st.session_state:
        st.session_state['montrer']=True  #création d'une variable qui bloque / débloque l'affichage de la solution

    with col2:   #partie droite
        b= st.container(height=500)  #création d'une 'boîte' de hauteur 500
        with b:    #dans cette boîte...       
            if st.session_state['montrer']==True:    #si l'affichage de la réponse est débloqué...
                st.write('Voici 5 mots de couleur: Vous avez 8 secondes pour les mémoriser')  #écrire consigne
                for i in st.session_state['sol']:  #faire défiler la liste contenant la solution et écrire chaque mot de la liste
                    st.write(i)
                time.sleep(8)  #attendre 8 secondes (pour laisser le temps au joueur de voir les mots)
                st.session_state['montrer']=False  #bloquer l'affichage de la solution
                st.rerun()  #rerun pour rafraichir la page (et donc masquer la solution)
            elif st.session_state['resultat']=="gagne" or st.session_state['resultat']=="perd":   #si le résultat du jeu est déterminé, afficher la solution
                for i in st.session_state['sol']:
                    st.write(i)
            else:   #sinon, afficher ?????????? (avec un ? pour chaque mot à trouver)
                for i in st.session_state['sol']:
                    st.write('?')
    with col1:  #partie gauche
        a= st.container(height=500)  #création d'une 'boîte' de hauteur 500
        with a:   #dans cette boîte...
            if st.session_state['resultat']==None:  #si le résultat n'est pas encore déterminé...
                col3, col4 = st.columns(2)  #séparation de la boîte en 2 colonnes
                m= round(len(st.session_state['prop'])/2)  #calculer la longueur de la liste de propositions et la diviser par 2, et stocker le résultat dans une variable
                with col3:  #colonne de gauche
                    for i in range(0,m):  #boucle bornée qui commence à 0 et finit à m-1
                        if st.button(st.session_state['prop'][i]) and len(st.session_state['rep'])<len(st.session_state['sol']):
                            st.session_state['rep'].append(st.session_state['prop'][i])
                with col4: #colonne de droite
                    for i in range(m,len(st.session_state['prop'])):  #boucle bornée qui commence à m et finit à la longueur de la liste de propositions
                        if st.button(st.session_state['prop'][i]) and len(st.session_state['rep'])<len(st.session_state['sol']):
                            st.session_state['rep'].append(st.session_state['prop'][i])
                    
                st.write(f"Votre réponse: {st.session_state['rep']}")  #affichage de la réponse donnée par le joueur
                if st.button("Supprimer"):  #création d'un bouton permettant de réinitialiser la réponse du joueur
                    st.session_state['rep']=[]
                    st.rerun()
                if len(st.session_state['rep'])==len(st.session_state['sol']):  #si la longueur de la réponse donnée est la même que la solution...
                    if st.button("Valider"):   #créer un bouton Valider
                        #mettre les listes réponse et solution dans l'ordre alphabétique (pour ne pas se préoccuper de l'ordre
                        st.session_state['rep'].sort()
                        st.session_state['sol'].sort()
                        if st.session_state['rep'] == st.session_state['sol']:  #si la liste réponse donnée est la même que la solution, le résultat est "gagne"
                            st.session_state['resultat']="gagne"
                        else:   #sinon, le résultat est "perd"
                            st.session_state['resultat']="perd"
                        st.rerun()  #rerun pour actualiser (et donc afficher le résultat)
            else: #si le résultat est déterminé...
                if st.session_state['resultat']=="gagne":  #si le résultat est "gagne", écrire "Gagné !" et appeler la fonction gagne() qui augmente l'humeur et met une animation de ballons
                    st.write("Gagné !")
                    gagne()
                elif st.session_state['resultat']=="perd":   #si le résultat est "perd", écrire "Perdu..." et appeler la fonction perd() qui augmente l'humeur (mais moins que gagne())
                    st.write("Perdu...")
                    perd()
                if st.button('Rejouer'):   #création d'un bouton Rejouer qui, lorsqu'il est cliqué, réinitialise les variables cookies et fait donc recommmencer le jeu
                    st.session_state['sol']=None
                    st.session_state['prop']=None
                    st.session_state['rep']=None
                    st.session_state['resultat']=None
                    st.session_state['montrer']=True
                    time.sleep(1)
                    st.rerun()