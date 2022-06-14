from tkinter import *
import random
from turtle import delay
import Kanas
from tkinter import ttk

kana, phonetique = random.choice(list(Kanas.dictionnaire.items()))
bonne_rep = 0
mauvaise_rep = 0

#Initialisation de la fenêtre
fenetre = Tk()
#fenetre.iconbitmap("/assets/icone.ico")
fenetre.title("Kana training")
fenetre.configure(width=1000, height=600)
caractere=Label(fenetre, text=kana, font='Arial 120 bold')
caractere.place(relx=0.5, rely=0.3, anchor=CENTER)
aide=Label(fenetre, text="", font='Arial 40 bold')
aide.place(relx=0.5, rely=0.65, anchor=CENTER)
fenetre.resizable(False, False)


#Boite de saisie
saisie = Entry(fenetre, width=10, font='Arial 25 bold')
saisie.place(relx=0.5, rely=0.5, anchor=CENTER)
barre = ttk.Progressbar(fenetre, orient=HORIZONTAL, length=200, mode='determinate')
barre.place(relx=0.5, rely=0.8, anchor=CENTER)
barre['value'] = 0

#Décompte de 5 secondes avant de passer au nouveau kana
def countdown():
    if barre['value'] < 100:
        barre['value'] += 1
        fenetre.after(50, countdown)
    if barre['value'] == 100:
        nouveau_kana()

def resultats():
    texte_bonne_reponse = Label(fenetre, text="Bonnes réponses : " + str(bonne_rep), font='Arial 15 bold')
    texte_bonne_reponse.place(relx=0, rely=0, anchor=NW)
    texte_mauvaise_reponse = Label(fenetre, text="Mauvaises réponses : " + str(mauvaise_rep), font='Arial 15 bold')
    texte_mauvaise_reponse.place(relx=0, rely=0.07, anchor=NW)

#Fonction qui génère un nouveau kana
def nouveau_kana():
    global kana, phonetique, barre
    barre['value'] = 0
    kana, phonetique = random.choice(list(Kanas.dictionnaire.items()))
    caractere.configure(text=kana)
    saisie.delete(0, END)
    saisie.configure(state='normal')
    aide.configure(text="")
    print("Kana : " + kana + " Phonétique : " + phonetique)

#bloque la saisie et la barre de progression pendant 2 secondes
def bloque_saisie():
    var = IntVar()
    fenetre.after(0, var.set, 1)
    barre['value'] -= 1000
    saisie.configure(state='disabled')
    fenetre.after(800, nouveau_kana)

#Detecte si la touche entrée est pressée, si la valeur saisie est correcte passer au kana suivant, sinon, change la valeur texte du label resultat en "Réesaye"
def detecte_touche(event):
    global kana, phonetique, barre, bonne_rep, mauvaise_rep
    valeur_saisie = saisie.get().lower()
    if event.keysym == "Return":
        if valeur_saisie == phonetique:
            print("Réponse correcte")
            bonne_rep += 1
            nouveau_kana()
            resultats()
        else:
            print("Réponse incorrecte")
            aide.configure(text=phonetique)
            saisie.delete(0, END)
            mauvaise_rep += 1
            resultats()
            bloque_saisie()





nouveau_kana()
resultats()
countdown()









fenetre.bind('<Return>', detecte_touche)

fenetre.mainloop()

