#!/usr/bin/python3
# 6-print_matrix_integer.py
def print_matrix_integer(matrix=[[]]):
	for row in matrix:
		print(" ".join("{:d}".format(item) for item in row))
