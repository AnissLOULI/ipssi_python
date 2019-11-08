#!/usr/bin/python3

import os
apath = os.path.expanduser("~/Documents/gits/exam2/ex05/docker-compose.yml")
print ("chemin etendu en", apath)

fichier = open("docker-compose.yml", "r")
for line in fichier:
	print(line)
fichier.close()
