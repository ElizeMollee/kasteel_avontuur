import states

def begin():
    
    print("Je staat voor een groot kasteel. De poort staat op een kier.")
    print("Ga je naar BINNEN of loop je terug naar het BOS?")
    keuze = input("> ")

    if keuze == "BINNEN":
        states.locatie = "BINNENPLAATS"
    
    elif keuze == "BOS":
        print("Je loopt terug het bos in. Het avontuur eindigt.")
        states.spel_bezig = False  

