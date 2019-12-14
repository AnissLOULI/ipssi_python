#!/usr/bin/python3



import sys
import os
import shutil
from datetime import datetime

def clean_downloads(dossier):
    
    liste_fichier = os.listdir(dossier)
    
    if len(liste_fichier) == 0:
        print ('Aucun fichier dans ce dossier !')
    else:
        print("cleanup old files : (more than 10 days + 50MB)\n")
        for fichier in liste_fichier:
            jours_depuis_creation = (datetime.now() - datetime.fromtimestamp(os.stat(dossier+fichier).st_atime)).days
            taille_fichier = os.stat(dossier+fichier).st_size
            if jours_depuis_creation > 10 or taille_fichier > 6250000:
                print(fichier)
                choix = input("[yes/No]?")
                if choix == "yes":
                    os.remove(dossier+fichier)
                    print(fichier+" delete\n")
                else:
                    print(fichier+" keep\n")
            else:
                print(fichier)
                print("organizing your files :")
                a = str(datetime.fromtimestamp(os.stat(dossier+fichier).st_atime).year)+"-"+str(datetime.fromtimestamp(os.stat(dossier+fichier).st_atime).month)
                try:
                    os.mkdir(dossier+a)
                except:
                    print("dossier déja exitant")
                print("moving into "+a+" : "+fichier+"\n") 
                shutil.move(dossier+fichier,dossier+a)

                    
                

    return "end"
        
if __name__ == "__main__":
    print(clean_downloads(sys.argv[1]))