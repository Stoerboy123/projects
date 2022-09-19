from random import choice
from sys import exit 

acties = ["steen","papier","schaar"]

def kies_actie():
    actie = input("Kies: 1 voor steen, 2 voor papier, 3 voor schaar.\nTyp exit om te stoppen.\n> ")
    
    if actie == "1":
        actie = "steen"
    elif actie == "2":
        actie = "papier"
    elif actie == "3":
        actie = "schaar"
    elif actie == "exit":
        exit()
    else:
        print("Leer typen sukkel!")
        kies_actie()

    return actie

    
while True:
    actie = kies_actie()
    print(f"Jouw keuze: {actie}")
    
    ai_actie = choice(acties)
    
    print(f"De ai's keuze: {ai_actie}")
    
    if actie == ai_actie:
        print("GELIJKSPEL")
    if (actie == "steen" and ai_actie == "schaar") or (actie == "schaar" and ai_actie == "papier") or (actie == "papier" and ai_actie == "steen"):
        print("JE HEBT GEWONNEN")
    if (actie == "papier" and ai_actie == "schaar") or (actie == "steen" and ai_actie == "papier") or (actie == "schaar" and ai_actie == "steen"):
        print("JE HEBT NIET GEWONNEN >:(")
