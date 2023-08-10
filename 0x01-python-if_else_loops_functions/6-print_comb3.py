#!/usr/bin/python3

for num in range(0, 10):

    for j in range((1+num), 10):

        print("{:x}{:x}".format(num, j), end="")

        if num != 8 or j != 9:
            print(", ", end="")
print("".format("\n"))
