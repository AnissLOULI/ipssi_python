#!/usr/bin/python3

import os
apath = os.path.expanduser("~/Documents/gits/exam2/ex05/docker-compose.yml")

image = 'image'
fichier = open("docker-compose.yml", "r")
for line in fichier:
	if image in line:
		print(line.strip().split()[1])
fichier.close()
