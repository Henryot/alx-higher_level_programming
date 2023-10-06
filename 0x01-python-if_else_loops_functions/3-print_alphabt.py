#!/usr/bin/python3
for char in range(97, 123):
    if char != 101 and char != 113:  # 101 is 'e' and 113 is 'q'
        print("{}".format(chr(char)), end='')
