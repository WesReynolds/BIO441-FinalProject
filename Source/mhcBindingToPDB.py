THRESHOLD = 10
dataSourceFilepath = "../ProgramData/large_example.csv"
epitope = "LFHIFDGDNEI"

# This method reads a file that contains the output of the IEDB MHC I program.
# 
# From this file, the alleles that have an affinity score within a certain threshold
# are printed to stdout in a PDB format.


def main():
    dataFp = open(dataSourceFilepath, "r")
    line = dataFp.readline()
    line = dataFp.readline()

    first = True
    while line != "":
        tokens = line.split(",")
        allele = tokens[0]
        percentile = float(tokens[-1])
        if percentile < THRESHOLD:
            if first:
                print(epitope + "\t" + allele, end="")
                first = False
            else:
                print("," + allele, end="")
        line = dataFp.readline()


# Driver routine for main program
if __name__ == "__main__":
    main()
