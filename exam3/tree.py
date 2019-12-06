import sys
from math import *

def show_tree (largeur_du_sapin):
    hauteur_tronc = floor ((largeur_du_sapin / 5)) + 1
    
    if (largeur_du_sapin % 2 == 0):
        largeur_du_sapin = largeur_du_sapin + 1

    if largeur_du_sapin < 4:
        tronc = 1
    else:
        tronc = 3
    
    sapin = ""
    
    for i in range (1, largeur_du_sapin + 1, 2):
        sapin = sapin + (i * "x").center(largeur_du_sapin)
        sapin = sapin + "\n"
    
    for i in range (hauteur_tronc):
        if (i < hauteur_tronc - 1):
            sapin = sapin + (tronc * "x").center(largeur_du_sapin)
            sapin = sapin + "\n"
        else:
            sapin = sapin + (tronc * "x").center(largeur_du_sapin)
    
    return sapin


if __name__ == "__main__":
    print(show_tree(int(sys.argv[1])))
