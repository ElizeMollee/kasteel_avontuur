import states

def begin():
    
    print("In de kamer ligt een glimmende sleutel.")
    print("Wil je de SLEUTEL pakken of TERUG gaan?")
    keuze = input("> ")

    if keuze == "SLEUTEL":
        states.heeft_sleutel = True
        print("Je neemt de sleutel mee.")
        states.locatie = "BINNENPLAATS"
    elif keuze == "TERUG":
        states.locatie = "BINNENPLAATS"
