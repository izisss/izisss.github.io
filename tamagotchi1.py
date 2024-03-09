#importation des bibliothèques et des fichiers nécessaires
import streamlit as st
from jeux import *
from pendu import *
from gagne_perd import *
from memoire import *
import random
import time

if 'situation' not in st.session_state: #initialisation de la situation si cela n'est pas déjà fait
    st.session_state['situation'] = "presentation" #au premier démarrage, on lui donne la valeur "présentation"

if st.session_state['situation'] =="presentation": #si la situation est présentation, afficher un message explicatif
    st.balloons() #animation de ballons
    st.title("Bienvenue sur notre Tamagotchi en ligne")
    st.divider()
    st.write("Vouz devrez vous occuper de votre tamagotchi afin qu'il ne meure pas.")
    st.markdown('*Vous devrez gérer :*') 
    st.markdown('* son humeur')
    st.markdown('* son alimentation')
    st.markdown('* son sommeil')
    st.markdown('* sa santé')
    st.markdown('* son hygiène')
    if st.button('Commencer 🌼'): #bouton pour démarrer le jeu
        st.session_state['situation'] ="debut" #on change la valeur de situation en "début" pour passer à l'étape  suivante
        st.rerun() #rerun pour reprendre le programme depuis le début (comme on a changé le cookie 'situation', on passe à la prochaine étape)

if st.session_state['situation'] =="debut": #si la situation est 'début'
    if 'choix_oeuf' not in st.session_state: #initialisation de la variable 'choix_oeuf' qui sotckera les images correspondant à l'oeuf choisi
        st.session_state['choix_oeuf'] = None
    st.title('Configurez votre animal virtuel')#titre
    col1,col2,col3=st.columns(3)#division de la page en 3 colonnes
    
    #dictionnaire pour chaque oeuf avec les liens pour chaque évolution/ émotion
    oeuf_1={'image_oeuf':'https://tamagotchi.com/wp-content/uploads/Creative.jpg' , 'image_animal':"cochon1.png" , 'heureux': "cochon2.png", 'normal':"cochon1.png", 'mal':"cochon3.png", 'laver':"laver.gif", 'dodo':"conchong.gif", 'texte':"C'est un cochon 🐷"}
    oeuf_2={'image_oeuf':'https://tamagotchi.com/wp-content/uploads/Creative.jpg' , 'image_animal':"poulpe1.png" , 'heureux': "poulpe3.png", 'normal':"poulpe1.png", 'mal':"poulpepleur.png", 'laver':"laver_p.gif", 'dodo':"poulpeg.gif", 'texte': "C'est un poulpe 🐙"}
    oeuf_3={'image_oeuf':'https://tamagotchi.com/wp-content/uploads/Creative.jpg' , 'image_animal':"pingouin1.png" , 'heureux': "pingouinh.png", 'normal':"pingouin1.png", 'mal':"pingouinpleur.png", 'laver':"laver_ping.gif", 'dodo':"pingouin_dodoo.gif", 'texte': "C'est un pingouin 🐧"}
    if st.session_state['choix_oeuf']==None: #si aucun oeuf n'a été choisi
        with col1: #dans la première colonne...
            #premier oeuf + bouton de choix
            st.image(oeuf_1['image_oeuf']) #image de l'oeuf contenue dans le dictionnaire du premier oeuf
            if st.button('Oeuf n°1'): #si le bouton est cliqué
                st.session_state['choix_oeuf']=oeuf_1 #associer à la variable 'choix_oeuf' le dictionnaire oeuf_1
                st.rerun() #rerun pour actualiser
        with col2: #même chose pour col2 (avec le 2e oeuf) et col3 (avec le 3e oeuf)
            #deuxième oeuf + bouton de choix
            st.image(oeuf_2['image_oeuf'])
            if st.button('Oeuf n°2'):
                st.session_state['choix_oeuf']=oeuf_2
                st.rerun()
        with col3:
            #troisième oeuf + bouton de choix
            st.image(oeuf_2['image_oeuf'])
            if st.button('Oeuf n°3'):
                st.session_state['choix_oeuf']=oeuf_3
                st.rerun()
        st.write('')#sauter une ligne
        st.write("Dans chacun de ces oeufs se trouve un adorable compagnon... Choisissez le votre !") #message explicatif

    if st.session_state['choix_oeuf']!=None: #si un oeuf a été choisi
        with col2: #(dans la colonne du milieu)
            st.image(st.session_state['choix_oeuf']['image_animal']) #afficher l'image de l'animal associée à l'oeuf choisi
        st.session_state['nom'] = st.text_input("Choisis le nom de ton animal") #saisie du nom
        if st.session_state['nom']!="": #affichage d'un message et d'un bouton de validation si un nom est entré
            st.write(f"Clique sur 'Confirmer' pour commencer la partie. Prend bien soin de {st.session_state['nom']} !")
            if st.button("Confirmer"):
                st.session_state['situation'] ="normal" #changement de situation si le bouton est cliqué
                time.sleep(1) #attendre 1sec (permet d'éviter les bugs d'affichage)
                st.rerun() #rerun pour actualiser
            

if st.session_state['situation'] == "normal":   #interface avec les barres d'état
    st.title("Mode Normal")   #titre de la page

    col1, col2=st.columns(2)   #division de la page en 2
    #initialisation des variables cookies
    if 'humeur' not in st.session_state or st.session_state['humeur'] ==None:
        st.session_state['humeur'] = 10  #humeur
    if 'nourriture' not in st.session_state or st.session_state['nourriture']==None:
        st.session_state['nourriture']=8  #faim
    if 'sommeil' not in st.session_state or st.session_state['sommeil']==None:
        st.session_state['sommeil']=9   #sommeil
    if 'dormir' not in st.session_state or st.session_state['dormir']==None:
        st.session_state['dormir']=False   #afficher l'animation (ou pas)
    if 'hygiène' not in st.session_state or st.session_state['hygiène']==None:
        st.session_state['hygiène']=5  #hygiène
    if 'laver' not in st.session_state or st.session_state['laver']==None:
        st.session_state['laver']=False   #afficher l'animation (ou pas)
        
    with col1:   #partie gauche
        a=st.container(height=500)   #'boîte' dans laquelle on met l'image de notre animal
        with a:  
            if st.session_state['dormir']==True:  #si variable d'animation vraie, afficher le gif correspondant
                st.image(st.session_state['choix_oeuf']['dodo'])
            elif st.session_state['laver']==True:
                st.image(st.session_state['choix_oeuf']['laver'])
                time.sleep(5)   #laisser le gif 5 secondes
                st.session_state['hygiène']=10   #on remet ensuite la jauge d'hygiène au maximum
                st.session_state['laver']=False  #arreter l'animation
                st.rerun()
            elif st.session_state['humeur']>=8 and st.session_state['hygiène']>=8 and st.session_state['nourriture']>=8 and st.session_state['sommeil']>=9:   #si tout va bien, mettre l'image de l'animal heureux
                st.image(st.session_state['choix_oeuf']['heureux'])
            elif st.session_state['humeur']<=3 or st.session_state['hygiène']<=3 or st.session_state['nourriture']<=3 or st.session_state['sommeil']<=3:    #si tout va mal, mettre l'image de l'animal triste
                st.image(st.session_state['choix_oeuf']['mal'])
            else: #sinon, mettre l'image normale
                st.image(st.session_state['choix_oeuf']['normal'])
    with col2:   #partie droite de l'écran
        #on crée 3 boîtes b, d et c de tailles différentes
        b=st.container(height=100)
        d=st.container(height=150)
        c=st.container(height=250)
        with b:  #boîte du haut
            st.write(f"Mon nom est {st.session_state['nom']}, j'ai hâte de te connaître !")  #message dans lequel le tamagotchi rappelle son nom
            #affichage d'un message différent en focntion des besoins du tamagotchi
            if st.session_state['humeur']<=4:
                st.write("J'ai besoin de jouer 🎮")
            elif st.session_state['hygiène']<=4:
                st.write("J'ai besoin de me laver 🛁")
            elif st.session_state['nourriture']<=4:
                st.write("J'ai besoin de manger 🥞")
            elif st.session_state['sommeil']<=4:
                st.write("J'ai besoin de dormir 🛏")
        with d:  #boite du milieu
            colg, cold= st.columns(2)   #division de la boite en 2
            with colg:  #partie gauche
                if st.button("Jeux"):   #création d'un bouton 'Jeux' qui change la situation et rerun pour renvoyer sur le choix du jeu
                    st.session_state['situation']="jeux"
                    st.rerun()
                if st.button("Nourrir") and st.session_state['nourriture'] <10:  #création d'un bouton 'Nourrir' qui augmente la jauge de nourriture
                    st.session_state['nourriture']+=1
                    time.sleep(0.1)
                
            with cold:  #partie droite
                if st.button("Dormir"):   #création d'un bouton 'Dormir' qui lance l'animation correspondante
                    st.session_state['dormir']=True
                    st.rerun()
                if st.session_state['dormir']==True:  #augmentation progressive de la jauge de sommeil puis arret de l'animation
                    for i in range(5):
                        if st.session_state['sommeil']<10:
                            st.session_state['sommeil']+=1
                        time.sleep(1)
                    st.session_state['dormir']=False
                    st.rerun()
                if st.button("Laver"):   #création d'un bouton 'Laver' qui lance l'animation correspondante
                    time.sleep(0.5)
                    st.session_state['laver']=True
                    st.rerun()
        with c:  #boite du bas
            st.write("Etat du Tamagotchi") #message indiquant la fonction des jauges

            #jauges correspondant à chaque variable d'état
            bar_humeur = st.progress(st.session_state['humeur'], text="Humeur")
            bar_nourriture = st.progress(st.session_state['nourriture'], text="Nourriture")
            bar_sommeil = st.progress(st.session_state['sommeil'], text="Sommeil")
            bar_hygiène = st.progress(st.session_state['hygiène'], text="Hygiène")
            bar_humeur.progress(st.session_state["humeur"]*10, text="Humeur")
            bar_nourriture.progress(st.session_state["nourriture"]*10, text="Nourriture")
            bar_sommeil.progress(st.session_state["sommeil"]*10, text="Sommeil")
            bar_hygiène.progress(st.session_state["hygiène"]*10, text="Hygiène")
            
            time.sleep(15) #15 secondes avant d'actualiser les variables
            st.session_state['humeur']-=1
            st.session_state['nourriture']-=1
            st.session_state['sommeil']-=1
            st.session_state['hygiène']-=1
            #si aucune des variables n'est tombée à 0, rerun
            if st.session_state['humeur']>0 and st.session_state['nourriture'] >0 and st.session_state['sommeil'] >0 and st.session_state['hygiène'] >0:
                st.rerun()
            else:  #sinon, changer la situation en "mort" et rerun pour changer de page
                st.session_state["situation"]="mort"
                st.rerun()
 

if st.session_state['situation'] =="jeux":  #si la situation est "jeux"
    st.title("A quoi voulez-vous jouer ? 🎲")  #titre de la page
    st.divider()
    col1, col2, col3=st.columns(3)  #division de la page en 3
    #pour chaque partie, création d'un bouton renvoyant à chaque jeu, affichage d'une image et d'une description correspondant
    with col1:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Pile_ou_face.png/170px-Pile_ou_face.png', width= 124)  
        if st.button("Pile ou face"):
            st.session_state['situation'] = "pile_ou_face"
            st.rerun()
        st.write(":violet[Choisissez entre pile ou face, c'est du hasard]")
    with col2:
        st.image('data:image/png;base64,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')
        if st.button("Jeu du Pendu"):
            st.session_state['situation'] = "pendu"
            st.rerun()
        st.write(':violet[Trouvez le mot mystère en appuyant sur le clavier]')
    with col3:
        st.image('https://static.vecteezy.com/ti/vecteur-libre/p3/20900880-facile-icone-humain-cerveau-vectoriel.jpg')
        if st.button("Jeu de mémoire"):
            st.session_state['situation'] = "memoire"
            time.sleep(1)
            st.rerun()
        st.write(':violet[Mémorisez la couleur et le mot et restituez-les]')
    if st.button("Retour au mode 'normal'"):  #bouton pour revenir au mode avec les jauges etc
        st.session_state['situation']='normal'
        time.sleep(1)
        st.rerun()
    

if st.session_state['situation'] =="pile_ou_face":   #si la situation est "pile ou face", appel de la fonction lançant le jeu de pile ou face
    jeux()

if st.session_state['situation'] =="pendu":   #si la situation est "pendu", appel de la fonction lançant le jeu de pendu
    st.title("Jeu du Pendu")
    pendu()
    if st.button("Retour au mode 'jeux'"):  #bouton de retour au choix du jeu
        st.session_state['situation']='jeux'
        st.session_state['affichage']=None
        time.sleep(1)
        st.rerun()

if st.session_state['situation'] =="memoire":  #si la situation est "memoire", appel de la fonction lançant le jeu de mémorisation
    st.title("Jeu de mémoire")
    memoire()
    if st.button("Retour au mode 'jeux'"):
        st.session_state['situation']='jeux'
        st.session_state['affichage']=None
        time.sleep(1)
        st.rerun()


if st.session_state['situation'] =="mort":  #si la situation est "mort", indiquer au joueur que son tamagotchi est mort et proposer de rejouer
    st.title('⚰️ Votre Tamagotchi est mort ⚰️')
    st.divider()
    col1, col2, col3=st.columns(3)
    with col2:
        st.image('https://media.tenor.com/63qpvQw4crUAAAAM/dead.gif')
    st.write('Si vous souhaitez recommencer une partie et retenter votre chance, appuyez sur le bouton "redémarrer"')

    if st.button("Redémarrer"):   #bouton pour rejouer qui réinitialise les variables cookie (sans pour autant afficher la page d'explication qui n'apparait alors qu'à la première connexion)
        st.session_state['situation']='debut'
        st.session_state['humeur']=None
        st.session_state['nourriture']=None
        st.session_state['choix_oeuf']=None
        st.session_state['nom']=None
        st.session_state['sommeil']=None
        st.session_state['hygiène']=None
        st.rerun()
