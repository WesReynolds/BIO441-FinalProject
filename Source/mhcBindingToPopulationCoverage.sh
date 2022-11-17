allelesPDB="../ProgramData/targetAlleles.pdb"
popCovTool="../IEDB_population_coverage/calculate_population_coverage.py"
popCovOutput="../ProgramData/populationCoverageOutput.txt"
formattedPopCov="../ProgramData/formattedPopulationCoverage.txt"
bindingDataDir="../ProgramData/BindingData/"

# Using a directory containing MHC Binding data in a csv format, create a PDB file
# of all the alleles with a binding affinity rank above a threshold.
python mhcBindingToPDB.py $bindingDataDir 10 > $allelesPDB

# Generate the Population Coverage report. Writes data to console and to csv file.
python $popCovTool -p Japan,China,Brazil -c I -f $allelesPDB > $popCovOutput
python reformatPopulationCoverage.py $popCovOutput
python reformatPopulationCoverage.py $popCovOutput > $formattedPopCov
python calculateAverageHits.py $formattedPopCov
