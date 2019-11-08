#!/usr/bin/python3

import json

with open("students.json") as text:
	contenu = json.load(text)
	print(contenu)

