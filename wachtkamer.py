import states

def begin():
   
    if states.bewaker_afgeleid == False:
        print("Een bewaker kijkt je streng aan. Je kunt hier niet zomaar voorbij.")
        print("Ga je FLUITEN om hem af te leiden of ga je TERUG?")

        keuze = input("> ")

        if keuze == "FLUITEN":
            states.bewaker_afgeleid = True
            print("De bewaker rent weg om te zoeken waar het geluid vandaan komt!")
        elif keuze == "TERUG":
            states.locatie = "BINNENPLAATS"
    elif states.bewaker_afgeleid == True:
        print("De bewaker is weg. Er is een deur naar een TUNNEL.")
        print("Ga je naar de TUNNEL of TERUG?")
        keuze = input("> ")

        if keuze == "TUNNEL" and states.heeft_sleutel:
            states.locatie = "TUNNEL"
        elif keuze == "TUNNEL" and states.heeft_sleutel == False:
            print("De deur blijft op slot. Je hebt nog steeds een sleutel nodig!")
            states.locatie = "BINNENPLAATS"
        elif keuze == "TERUG":
            states.locatie = "BINNENPLAATS"
