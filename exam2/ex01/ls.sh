#!/bin/bash

if [ -e $1 ]; then
	ls -la $1 >> /tmp/ls.log
	echo "ls ok"
else
	echo 'ls: cannot acces '"$1"': No such file or directory' >> /tmp/ls_err.log
	echo "ls FAIL"
fi
