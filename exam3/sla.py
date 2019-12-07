#!/usr/bin/python3

import sys
import time

def show_sla (pourcentage):
    indisp_en_sec = 3600 * 24 * 365.25 * ((100 - pourcentage) / 100)
    heure = int (indisp_en_sec / 3600)
    minute = int (indisp_en_sec % 3600 / 60)
    seconde = int (indisp_en_sec % 3600 % 60)

    return ("{}h {}m {}s".format(heure, minute,seconde))


if __name__ == "__main__":
    print(show_sla(float(sys.argv[1])))