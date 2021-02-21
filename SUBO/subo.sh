#!/bin/bash
python3 sep.py 						      # separates the input file in 2 as needed for lalign36
~/fasta-36.3.8h/bin/lalign36 -m8 pattern1 pattern2 > results  # generates alignment data
params=$(awk -f subseq_select.awk results)		      # selects the substring from alignment data
python3 count_instances.py $params 			      # counts instances of that substring, intentional word splitting of params
