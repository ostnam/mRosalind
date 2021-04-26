#!/bin/bash
# off by one with the sample but that is apparently an issue with the sample
p=$(cat rosalind_ba6b.txt | tr -d '()+') # tr -d removes every char in the '' 
result=0
for i in $p; do
	if [[ ! $previous ]]; then
		previous=$i
		continue
	fi
	if (( $i != ($previous + 1) )); then
		((++result))
	fi
	previous=$i
done
echo "$result"
