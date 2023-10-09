#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
	return ''.join([char for char in my_string if char not in 'Cc'])

