#!/bin/bash
err_badparams="You didn't specify parameters correctly. There should be 2 positional arguments that are the name of the sequences to compare or a file named rosalind_need.txt with the names of the sequences."

# Verify positional arguments are specified properly
if [[ $# -ne 2 ]]; then
	if [[ -f "rosalind_need.txt" ]]; then
		set -- $(cat rosalind_need.txt)
	else
		echo "$err_badparams"
		exit 1
	fi
fi

# Download sequences using the python script if they aren't already available
for i in $1 $2; do
	if [[ ! -f "$i" ]]; then
		python3 need.py "$i"
	fi
done

# Compute the alignement score using the parameters given
# EMBOSS needs to be installed locally
needle "$1" "$2" -endweight -endopen=10 -endextend=1 -gapopen=10 -gapextend=1 -outfile "result"

echo "The final score is:"
grep "Score:" "result"
exit
