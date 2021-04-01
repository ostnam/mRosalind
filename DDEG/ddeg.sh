#!/bin/bash
# this solution is correct but does not scale to large file

result=""
edge_list=$(
	tail -n+2 rosalind_ddeg.txt
)

edges=$(
	echo "$edge_list" | sed 's/ /\n/' | sort -u
)
num_edges=$(
	head -n1 rosalind_ddeg.txt | mawk '{print $1}'
)

for h in $(seq "$num_edges"); do
	if grep -Fq -m 1 "$h" <<< "$edges"; then
		neighbours=$(
			echo "$edge_list" | grep -F "$h" 
		)
		neighbours=${neighbours//${h}}
		count=0
		for j in $neighbours; do
			let count+=$(echo "$edge_list" | grep -Fc "$j")
		done
		echo -n "${count} "
	else
		echo -n "0 "
	fi
done
echo
exit 0
