# Examen du 8 nov 2019

# Description

Voici mes fichiers d'examen
* ex01 :

#!/bin/bash

if [ -e $1 ]; then
        ls $1 >> /tmp/ls.log
        echo "ls ok"
else
        ls $1 2 >> /tmp/ls_err.log
        echo"ls FAIL"
fi




* ex02
* ex03
