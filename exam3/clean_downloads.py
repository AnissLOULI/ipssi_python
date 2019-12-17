#!/usr/bin/python3



import sys
import os
import shutil
from datetime import datetime

def clean_downloads (dossier):
    
    liste_fichier = os.listdir (dossier)
    
    if len (liste_fichier) == 0:
        print ('No file in directory !')
    else:
        print ("cleanup old files : (more than 10 days + 50MB)\n")
        for fichier in liste_fichier:
            jours_depuis_creation = (datetime.now() - datetime.fromtimestamp(os.stat(dossier+fichier).st_mtime)).days
            taille_fichier = os.stat (dossier+fichier).st_size
            if jours_depuis_creation > 10 and taille_fichier > 6250000:
                print (fichier)
                choix = input ("[yes/No]?\n")
                if choix == "y":
                    os.remove (dossier+fichier)
                    print (fichier+" delete\n")
                else:
                    print("")
            else:
                if jours_depuis_creation > 10:
                    print (fichier)
                    print ("organizing your files :")
                    annee_mois_du_fichier = str(datetime.fromtimestamp(os.stat(dossier+fichier).st_atime).year)+"-"+str(datetime.fromtimestamp(os.stat(dossier+fichier).st_atime).month)
                    try:
                        os.mkdir (dossier+annee_mois_du_fichier)
                    except:
                        ligne_bidon = 0
                    print ("moving into "+annee_mois_du_fichier+" : "+fichier+"\n") 
                    shutil.move (dossier+fichier,dossier+annee_mois_du_fichier)
                


                    
                

    return "end"
        
if __name__ == "__main__":
    print(clean_downloads(sys.argv[1]))