python filterAlleles.py > ../ProgramData/sampleMHCOutput.txt
python ../IEDB_population_coverage/calculate_population_coverage.py -p Japan,China,Brazil -c I -f ../ProgramData/sampleMHCOutput.txt
