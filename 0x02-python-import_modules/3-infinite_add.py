#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    sum = 0

    if argc == 0:
        print("{}".format(sum))

    else:
        for i in range(1, argc + 1):
            sum += int(argv[i])
    print("{}".format(sum))
