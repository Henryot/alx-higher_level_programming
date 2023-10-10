#!/usr/bin/python3

def print_combinations():
    for i in range(10):
        for j in range(i + 1, 10):
            print("{:d}{:d}".format(i, j), end=", " if i < 8 or j < 9 else "\n")

if __name__ == "__main__":
    print_combinations()
