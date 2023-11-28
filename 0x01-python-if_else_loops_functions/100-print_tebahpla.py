#!/usr/bin/python3

for letr in range(122, 96, -1):
    if letr % 2 == 0:
        print("{}".format(chr(letr)), end="")
    else:
        print("{}".format(chr(letr-32)), end="")
