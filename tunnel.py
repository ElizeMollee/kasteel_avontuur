import states

def begin():
  
    if states.heeft_sleutel:
        print("Je gebruikt de sleutel om een deur te openen naar de vrijheid.")
        print("JE BENT ONTSNAPT!")
        states.spel_bezig = False
    elif states.heeft_sleutel == False:
        print("De deur is op slot. Je hebt een sleutel nodig!")
        states.locatie = "WACHTKAMER"
