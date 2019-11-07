#!/usr/bin/python3

import datetime

today=datetime.datetime.now().day

if today % 2 == 0 :
	print("Nous sommes le ",today," c'est un jour pair") 
else :
	print("Nous sommes le ",today," c'est un jour impair") 
