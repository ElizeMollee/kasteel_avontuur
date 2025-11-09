import states
import poort
import binnenplaats
import wachtkamer
import toren
import tunnel

while states.spel_bezig:
    if states.locatie == "POORT":
        poort.begin()
    elif states.locatie == "BINNENPLAATS":
        binnenplaats.begin()
    elif states.locatie == "WACHTKAMER":
        wachtkamer.begin()
    elif states.locatie == "TOREN":
        toren.begin()
    elif states.locatie == "TUNNEL":
        tunnel.begin()
