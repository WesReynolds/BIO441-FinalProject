import sys

outputFilepath = "../ProgramData/finalOutput.csv"

# string[] --> void
def main(argv):
    dataFp = open(argv[1], "r")
    outFp = open(outputFilepath, "w")

    line = dataFp.readline()
    while line != "":
        tokens = line.split()
        for token in tokens:
            print("{0: <22}".format(token), end="")
            outFp.write("%s," % token)
        print()
        outFp.write("\n")
        line = dataFp.readline()

# Driver routine for main program
if __name__ == "__main__":
    main(sys.argv)
