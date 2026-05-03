#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sys.argv
    if len(sys.argv) < 2:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:\n" \
        "1:", sys.argv[1])
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for n in range(1, len(sys.argv)):
            print("{}: {}".format(n, sys.argv[n]))
