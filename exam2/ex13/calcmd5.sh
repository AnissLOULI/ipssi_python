#!/bin/bash

echo "$1" | md5sum|cut -d  ' ' -f1

