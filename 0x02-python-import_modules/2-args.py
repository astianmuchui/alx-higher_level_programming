#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1

    if argc == 0:
        print("{0} arguments".format(argc))

    elif argc == 1:
        print("{0} argument".format(argc))
        print("{0}: {1}".format(argc, argv[1]))

    else:
        print("{0} arguments".format(argc))

        for i in range(1, len(argv)):
            print("{0}: {1}".format(i, argv[i]))
