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
