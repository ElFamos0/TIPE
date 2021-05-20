"""
Malo Damien 

Messagerie utilisant un mixte de cryptosystème RSA - AES 

"""

import tkinter as tk

fenetre = tk.Tk()

fenetre.title("Cryptage")

fenetre.geometry("700x300")

label = tk.Label(fenetre, text="Entrer votre message à coder : ")
label.pack()


textExample=tk.Text(fenetre, height=10)
textExample.pack()

def getTextInput():
    result=textExample.get("1.0","end")
    print(result)
    
btnRead=tk.Button(fenetre, height=1, width=10, text="Crypter", 
                    command=getTextInput)

btnRead.pack()

fenetre.mainloop()  