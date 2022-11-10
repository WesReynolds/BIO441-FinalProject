allelesPDB=../ProgramData/targetAlleles.pdb
popCovTool=../IEDB_population_coverage/calculate_population_coverage.py
popCovOutput=../ProgramData/populationCoverageOutput.txt

python mhcBindingToPDB.py > $allelesPDB
python $popCovTool -p Japan,China,Brazil -c I -f $allelesPDB > $popCovOutput
python reformatPopulationCoverage.py $popCovOutput
