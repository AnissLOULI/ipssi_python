#!/usr/bin/python3

import sys
import time
import math

def show_sla(pourcentage):
    indisponibilite=3600*24*365.25*((100-pourcentage)/100)
    heure = int(indisponibilite / 3600)
    minute = int(indisponibilite % 3600 / 60)
    seconde = int(indisponibilite % 3600 % 60)

    return ("{}h {}m {}s".format(heure, minute,seconde))


if __name__ == "__main__":
    print(show_sla(float(sys.argv[1])))