#!/usr/bin/python3

import os


image = 'image'
fichier = open("docker-compose.yml", "r")
for line in fichier:
	if image in line:
		print(line.strip().split()[1])
fichier.close()
