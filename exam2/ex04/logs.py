#!/usr/bin/python3

from datetime import datetime

def logthis(a):
	now = datetime.now()
	date_time = now.strftime("%Y-%m-%d %H:%M:%S")
	print(date_time, a)
	text = date_time + " " + str(a)
	fichier = open("python.log", "a")
	fichier.write(text + "\n")
	fichier.close()
