#!/usr/bin/python3

import sys

argument = sys.argv[1]

fichier = open(argument,"r")
n = 0

for line in fichier:
	n = n + 1
print(n)
