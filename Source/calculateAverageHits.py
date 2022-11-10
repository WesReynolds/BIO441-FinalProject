import sys

def getWeightedAvg(hitPercentages):
    total = 0

    for hitPercentage in hitPercentages:
        total += float(hitPercentage[0]) * float(hitPercentage[1]) / float(100)

    return total

# string[] --> void
def main(argv):
    dataFp = open(argv[1], "r")

    countries = {}
    findingCountries = True

    line = dataFp.readline()
    while line != "":
        tokens = line.split()
        if len(tokens) < 1:
            line = dataFp.readline()
            continue
        if tokens[0] == "population/area":
            if findingCountries:
                line = dataFp.readline()
                while line.split()[0] != "average":
                    countries[line.split()[0]] = []
                    line = dataFp.readline()
                findingCountries = False
            else:
                line = dataFp.readline()
                while line.strip() != "":
                    tokens = line.split()
                    countries[tokens[0]].append([tokens[1], tokens[2]])
                    line = dataFp.readline()

        line = dataFp.readline()

    percentages = []
    for country in countries.keys():
        percentages.append([country, getWeightedAvg(countries[country])])

    percentages = sorted(percentages, key=lambda x: x[1], reverse=True)

    print("population/area       epitope_hits")
    for percentage in percentages:
        print("{0: <22}".format(percentage[0]), end="")
        print("{0: <22}".format(percentage[1]))

# Driver routine for main program
if __name__ == "__main__":
    main(sys.argv)