#On importe les bibliothèques nécessaires (streamlit pour l'affichage, random pour le choix du mot, time pour le temps d'affichage des codes erreur et le fichier gagne_perd pour augmenter l'humeur du tamagotchi en fonction du résultat du jeu)
import streamlit as st
import random
import time
from gagne_perd import *

#création de la fonction appelée dans le fichier principal
def pendu():
    #initialisation des variables (utilisation de session_state pour celles qui doivent rester malgré les 'rerun()'
    if 'affichage' not in st.session_state or st.session_state['affichage']==None: #initialiser uniquement si ce n'est pas déjà fait
        st.session_state['tentatives'] = 7 #nombre d'erreurs max
        st.session_state['lettres_trouvees'] = "" #lettres trouvées par le joueur au cours de la partie
        st.session_state['erreurs'] = "" #lettres essayées mais pas dans le mot
        choix=["ORDINATEUR", "SOURIS", "ROTATION", "AVIATEUR","JAVELOT", "EXPLOITER", "ARAIGNEE", "PERSONNAGE", "AQUARIUM", "CORBEAU", "POUVOIR", "OBJECTIF", "NARRATEUR", "BILLARD", "TABOURET", "ENDIVE", "ORNITHORYNQUE", "FOURCHETTE", "RAGONDIN", "DISTANCE", "QUADRILLAGE", "NUAGEUX", "GOURDE", "ESTOMAC", "MONTAGNE", "ALPHABET", "APPARTEMENT", "BACON", "CAMPEMENT", "MATHEMATIQUES", "ANTICONSTITUTIONNELLEMENT", "JONQUILLE", "PENDU"] #mots possibles
        st.session_state['solution']=random.choice(choix) #choix d'un mot au hasard dans la liste
        st.session_state['affichage']= ("?"+" ")*len(st.session_state['solution']) #affichage (? ? ? ?) nb de '?'= nb de lettres dans le mot
    possible=["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"] #caractères valides (pour le text_input)
    col1, col2=st.columns(2) #séparation de l'écran en 2
    with col1: #à gauche: partie saisie utilisateur + affichage (_ _ _ _)
        a= st.container(height=300) #création d'un container pour la partie gauche
        with a: #dans le container a
            if st.session_state['solution']=="".join(x for x in st.session_state['affichage'] if x not in " "): #si le joueur a trouvé le mot (join() sert ici à enlever les espaces du mot trouvé car dans la solution il n'y en a pas)
                st.write("Gagné !") #indiquer au joueur le résultat
                st.write(f"Mot: {st.session_state['solution']}")
                gagne()#utiliser la fonction gagne() pour augmenter l'humeur du tamagotchi
                if st.button('Rejouer'): #création d'un bouton pour rejouer
                    st.session_state['affichage']=None #donner à la variable la valeur None (condition pour réinitialiser les variables-> voir ligne 10)
                    st.rerun()#rerun pour reprendre le programme depuis le début
            elif st.session_state['tentatives']>0: #sinon, si il reste des tentatives...
                st.write(st.session_state['affichage']) #afficher _ _ A _
                proposition = st.text_input("Proposez une lettre : ").upper() #saisie d'une lettre par l'utilisateur (mise en majuscule)
                if proposition !="" and st.button("Confirmer"): #bouton pour confirmer
                    if proposition in st.session_state['solution']: #si la proposition est dans le mot
                        st.session_state['lettres_trouvees'] += proposition #ajouter la proposition aux 'lettres_trouvees'
                    elif (proposition not in possible)or (len(proposition)>1): #si la proposition n'est pas valide (pas dans les caractères valides ou plus d'une lettre)
                        st.write("Caractère non valide") #message d'erreur
                        st.write("Remarque: ne pas mettre d'accent ou de cédille")
                        time.sleep(3)#laisser ce message 3 secondes avant de continuer
                    elif proposition in st.session_state['erreurs']: #sinon si la lettre a déjà été entrée et n'est pas dans le mot (évite de perdre des tentatives pour rien)
                        st.write("Déjà essayé !") #message d'erreur
                        time.sleep(2)
                    else:
                        st.session_state['erreurs'] += proposition #sinon, ajouter la lettre aux erreurs
                        st.session_state['tentatives']-=1 #retirer une tentative
                    #gestion de l'affichage du mot
                    if st.session_state['lettres_trouvees']=="": #si aucune lettre n'a été trouvée 
                        st.session_state['affichage'] = ("?"+" ")*len(st.session_state['solution']) #affichage: ? ? ? ? (car si on met seulement des underscores, streamlit supprime automatiquement les espaces et affiche "_____")
                    else: #sinon...
                        st.session_state['affichage'] = " "
                        for i in st.session_state['solution']: #utilisation boucle for pour afficher les lettres trouvées et les underscores au bon endroit
                            if i in st.session_state['lettres_trouvees']:
                                st.session_state['affichage'] += i + " "
                            else:
                                st.session_state['affichage'] += "_ "
                    st.rerun() #rerun pour mettre à jour après avoir cliqué sur le bouton
            else:
                st.write("Perdu !") #si le mot n'est pas trouvé et qu'il ne reste plus aucune tentative, indiquer au joueur qu'il a perdu
                st.write(f"Le mot était: '{st.session_state['solution']}'") #affichage de la solution
                perd() #appel de la fonction perd() qui augmente l'humeur du tamagotchi (mais moins que la fonction gagne())
                if st.button('Rejouer'): #bouton pour rejouer
                    st.session_state['affichage']=None
                    st.rerun()
    with col2: #partie droite de l'écran
        b= st.container(height=300)#création d'un container à gauche
        with b: #dans le container de droite...
            st.write(f"Tentatives restantes: {st.session_state['tentatives']}") #Affichage du nombre de tentatives restantes
            #image de pendu correspondante
            if st.session_state['tentatives']==0:
                st.image("images/p8.png")
            elif st.session_state['tentatives']==1:
                st.image("images/p7.png")
            elif st.session_state['tentatives']==2:
                st.image("images/p6.png")
            elif st.session_state['tentatives']==3:
                st.image("images/p5.png")
            elif st.session_state['tentatives']==4:
                st.image("images/p4.png")
            elif st.session_state['tentatives']==5:                    
                st.image("images/p3.png")
            elif st.session_state['tentatives']==6:
                st.image("images/p2.png")
            elif st.session_state['tentatives']==7:
                st.image("images/p1.png")