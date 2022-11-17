import sys
import os

# This method reads a file that contains the output of the IEDB MHC I program.
# 
# From this file, the alleles that have an affinity score within a certain threshold
# are printed to stdout in a PDB format.

def printPDBForEpitope(filepath, threshold):
    epitope = filepath.split("/")[-1].split(".")[0]
    inFP = open(filepath, "r")
    line = inFP.readline()
    line = inFP.readline()

    first = True
    while line != "":
        tokens = line.split(",")
        allele = tokens[0]
        percentile = float(tokens[-1])
        if percentile <= threshold:
            if first:
                print("%s\t%s" % (epitope, allele), end="")
                first = False
            else:
                print(",%s" % (allele), end="")
        line = inFP.readline()
    print()


def main(argv):
    bindingDataDir = argv[1]
    threshold = float(argv[2])
    for filename in os.listdir(bindingDataDir):
        printPDBForEpitope(bindingDataDir+filename, threshold)


# Driver routine for main program
if __name__ == "__main__":
    main(sys.argv)
