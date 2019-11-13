# Examen du 8 nov 2019

`Description`

Voici mes fichiers d'examen
* ex01 :

#!/bin/bash

if [ -e $1 ]; then  
        ls -la $1 >> /tmp/ls.log  
        echo "ls ok"  
else  
        echo 'ls: cannot acces '"$1"': No such file or directory' >> /tmp/ls_err.log  
        echo"ls FAIL"  
fi  

* ex02

#!/bin/bash

cut -d : -f3 /etc/passwd

* ex03

#!/usr/bin/python3

def multiplication(a, b):
	mult = a * b
	return mult

def division(a, b):
	if b == 0:
		print("sorry cannot divide by zero")
		div = 0
	
	else:
		div = a / b
	return div

* ex04

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
* ex05

#!/usr/bin/python3

import os


image = 'image'
fichier = open("docker-compose.yml", "r")
for line in fichier:
	if image in line:
		print(line.strip().split()[1])
fichier.close()

* ex06

#!/usr/bin/python3

import sys

argument = sys.argv[1]

fichier = open(argument,"r")
n = 0

for line in fichier:
	n = n + 1
print(n)

* ex07

#!/bin/bash

set -e

if curl -s -I www.google.com>/dev/null ;then
	echo $(date '+%Y-%m-%d:%H:%M:%S') internet ok>>internet.log
else
	echo $(date '+%Y-%m-%d:%H:%M:%S') internet FAIL>>internet.log
	exit 2
fi
exit 0

* ex08

#!/bin/bash

set -e

git status
git add .
git commit -m "$1"
git push

* ex10

#!/usr/bin/python3

import json

with open("students.json") as text:
	contenu = json.load(text)
	print(contenu)

* ex11

FROM alpine:3.9
CMD [ "sh" ]
RUN mkdir -p /ipssi

* ex12

version: '2.2'

services:
   db:
     image: mysql:5.7
     volumes:
       - db_data:/var/lib/mysql
     restart: always
     environment:
       MYSQL_ROOT_PASSWORD: somewordpress
       MYSQL_DATABASE: wordpress
       MYSQL_USER: wordpress
       MYSQL_PASSWORD: wordpress

   wordpress:
     depends_on:
       - db
     image: wordpress:5-php7.1-fpm-alpine
     ports:
       - "7777:80"
     restart: always
     environment:
       WORDPRESS_DB_HOST: db:3306
       WORDPRESS_DB_USER: wordpress
       WORDPRESS_DB_PASSWORD: wordpress
       WORDPRESS_DB_NAME: wordpress
volumes:
    db_data: {}

* ex13

#!/bin/bash

echo "$1" | md5sum|cut -d  ' ' -f1

* ex14

#!/bin/bash

docker run -it -v /tmp:/out ipssi/ex14:1 /bin/sh

* ex15

#!/usr/bin/python3

import sys
import hashlib

def compare_pass(argument):
	ipssi = 'ipssi'

	ipssi_hash = hashlib.md5(ipssi.encode()).hexdigest()
	print("md5 \"ipssi\" : ", ipssi_hash)

	pass_hash = hashlib.md5(argument.encode()).hexdigest()
	print("md5    pass : ", pass_hash)

	if ipssi_hash == pass_hash:
		return True
	else:
		return False

