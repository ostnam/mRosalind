#!/bin/bash
rna=$(
	tail -n+2 "rosalind_mmch.txt"
)
a_count=$(
	echo "$rna" | fold -w 1 | grep -ci "A"
)
c_count=$(
	echo "$rna" | fold -w 1 | grep -ci "C"
)
g_count=$(
	echo "$rna" | fold -w 1 | grep -ci "G"
)
u_count=$(
	echo "$rna" | fold -w 1 | grep -ci "U"
)
python3 mmch.py "$a_count" "$c_count" "$g_count" "$u_count"
