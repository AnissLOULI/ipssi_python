#!/usr/bin/python3



import sys
import os
from datetime import *


def clean_downloads(dossier):

    liste_fichier = os.listdir(dossier)
    print("cleanup old files: (more than 10 days + 50MB)\n")

    for fichier in liste_fichier:
        if os.stat(dossier+fichier).st_mtime > 864000 and os.stat(dossier+fichier).st_size > 6250000:
            print(fichier)
            choix = input('[yes/No]?')
    
    return 
    
if __name__ == "__main__":
    print(clean_downloads(sys.argv[1]))