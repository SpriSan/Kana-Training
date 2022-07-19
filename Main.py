from tabnanny import check
from tkinter import *
import random
from turtle import back, delay
import Kanas
from tkinter import ttk
import customtkinter


#ne vous plaignez pas si vous trouvez que ce fichier est un vrai bourbier


kana, phonetique = random.choice(list(Kanas.dictionnaire.items()))
bonne_rep = 0
mauvaise_rep = 0
countdown_actif = True
temps = 0
millisecondes = 0
couleur = '#66a7ff'
couleur2 = '#2b66b5'

#Initialisation de la fenêtre
fenetre = customtkinter.CTk()
fenetre.title("Kana training")
fenetre.configure(background=couleur)
fenetre.geometry("1000x600")
caractere=Label(fenetre, text=kana, font='Arial 120 bold')
caractere.place(relx=0.5, rely=0.3, anchor=CENTER)
caractere.configure(background=couleur)
aide=Label(fenetre, text="", font='Arial 40 bold')
aide.place(relx=0.5, rely=0.65, anchor=CENTER)
aide.configure(background=couleur)
fenetre.resizable(False, False)




#détecte si la checkbox est cochée ou décochée et change la valeur de la variable countdown_actif
def checkbox_clique():
    global countdown_actif
    if var.get() == True:
        countdown_actif = False
        print("Countdown déscativé")
        barre['value'] = 0
    if var.get() == False:
        print("Countdown activé")
        countdown_actif = True
        countdown()



var = BooleanVar(value=False)
checkbox = customtkinter.CTkCheckBox(fenetre, text='Désactiver la limite de temps', variable=var, text_color="black", text_font="Arial 10 bold", command=checkbox_clique, onvalue=True, offvalue=False, hover=False, border_color="Black")
checkbox.place(relx=0.5, rely=0.9, anchor=CENTER)
checkbox.configure(background=couleur)

#Boite de saisie
saisie = customtkinter.CTkEntry(fenetre, placeholder_text="", width=250, height=60, border_width=2, corner_radius=20, text_font="Arial 25 bold", placeholder_text_color="white", state='normal')
saisie.place(relx=0.5, rely=0.5, anchor=CENTER)

barre = ttk.Progressbar(fenetre, orient=HORIZONTAL, length=200, mode='determinate')
barre.place(relx=0.5, rely=0.8, anchor=CENTER)
barre['value'] = 0

timer = Label(fenetre, text="" + str(bonne_rep), font='Arial 30 bold')
timer.configure(background=couleur)
timer.place(relx=1, rely=0, anchor=NE)




#compteur de secondes et de millisecondes séparées par un point
def compteur():
    global millisecondes
    if millisecondes < 99:
        millisecondes += 1
        fenetre.after(1, compteur)
    else:
        millisecondes = 0
        fenetre.after(1, compteur)
        

def decompte():
    global temps
    if temps < 60:
        temps += 1
        fenetre.after(1000, decompte)


def update_timer():
    timer.configure(text=str(temps) + "." + str(millisecondes))
    fenetre.after(30, update_timer)

compteur()
decompte()


#Décompte de 5 secondes avant de passer au nouveau kana
def countdown():
    global mauvaise_rep
    if countdown_actif is True:
        if barre['value'] < 100:
            barre['value'] += 1
            fenetre.after(50, countdown)
        if barre['value'] == 100:
            aide.configure(text=phonetique)
            bloque_saisie()
            mauvaise_rep += 1
            resultats()
    if countdown_actif is False:
        barre['value'] = 0


def resultats():
    texte_bonne_reponse = Label(fenetre, text="Trouvés : " + str(bonne_rep), font='Arial 15 bold')
    texte_bonne_reponse.place(relx=0, rely=0, anchor=NW)
    texte_bonne_reponse.configure(background=couleur)
    texte_mauvaise_reponse = Label(fenetre, text="Non trouvés : " + str(mauvaise_rep), font='Arial 15 bold')
    texte_mauvaise_reponse.place(relx=0, rely=0.07, anchor=NW)
    texte_mauvaise_reponse.configure(background=couleur)


#Fonction qui génère un nouveau kana
def nouveau_kana():
    global kana, phonetique, barre
    barre['value'] = 0
    kana, phonetique = random.choice(list(Kanas.dictionnaire.items()))
    caractere.configure(text=kana)
    clear_saisie()   
    saisie.configure(state=NORMAL)
    aide.configure(text="")
    print("Kana : " + kana + " Phonétique : " + phonetique)

def clear_saisie():
    global saisie
    #Je suis obligé de faire que le programme recréer le module de saisie pour contrer un bug lié à CustomTkinter
    saisie.destroy()
    saisie = customtkinter.CTkEntry(fenetre, placeholder_text="", width=250, height=60, border_width=2, corner_radius=20, text_font="Arial 25 bold", placeholder_text_color="white", state='normal')
    saisie.place(relx=0.5, rely=0.5, anchor=CENTER)
    saisie.focus()


#bloque la saisie et la barre de progression pendant 2 secondes
def bloque_saisie():
    global saisie
    var = IntVar()
    fenetre.after(0, var.set, 1)
    saisie.configure(state=DISABLED)
    barre['value'] -= 1000
    fenetre.after(800, nouveau_kana)   


def detecte_touche(event):
    global kana, phonetique, barre, bonne_rep, mauvaise_rep, saisie
    valeur_saisie = saisie.get().lower()
    print(valeur_saisie)
    if event.keysym == "Return":
        if valeur_saisie == phonetique:
            print("Réponse correcte")
            bonne_rep += 1
            nouveau_kana()
            resultats()
            clear_saisie()            
        else:
            print("Réponse incorrecte")
            aide.configure(text=phonetique)
            mauvaise_rep += 1
            bloque_saisie()
            resultats()      
            


nouveau_kana()
resultats()
countdown()



fenetre.bind('<Return>', detecte_touche)


fenetre.mainloop()

