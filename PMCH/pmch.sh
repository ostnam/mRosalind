#!/bin/bash
rna=$(
	tail -n+2 "rosalind_pmch.txt"
)
a_count=$(
	echo "$rna" | fold -w 1 | grep -ci "A"
)
g_count=$(
	echo "$rna" | fold -w 1 | grep -ci "G"
)
python3 -c "from math import factorial;print(factorial($a_count)*factorial($g_count));"
# a_fac=1                         
# g_fac=1			  
# for i in $(seq 1 $a_count); do  
# 	let a_fac*=$i	          # this block does the same thing as the last
# done                            # line however bash cannot calculate high
# for i in $(seq 1 $g_count); do  # factorials without int overflows
# 	let g_fac*=$i	
# done
# result=$((a_fac*g_fac))
# echo "$result"
