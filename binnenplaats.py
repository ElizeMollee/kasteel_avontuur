import states

def begin():
   
    print("Je ziet een fontein en twee deuren.")
    print("Ga je naar de WACHTKAMER of naar de TOREN?")
    keuze = input("> ")

    if keuze == "WACHTKAMER":
        states.locatie = "WACHTKAMER"
    elif keuze == "TOREN":
        states.locatie = "TOREN"
