import sys

# string[] --> void
def main(argv):
    dataFp = open(argv[1], "r")
    line = dataFp.readline()
    while line != "":
        tokens = line.split()
        for token in tokens:
            print("{0: <22}".format(token), end="")
        print()
        line = dataFp.readline()

# Driver routine for main program
if __name__ == "__main__":
    main(sys.argv)
