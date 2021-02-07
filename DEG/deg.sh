#!/bin/bash
graph=$(tail -n +2 "$1")
nodes=$(echo "$graph" | sed 's/ /\n/g' | sort -n | uniq )
result=""

for i in $nodes; do
	result+=$(echo -n "$graph" | sed 's/ /\n/g' | grep -Ec "^$i$" | sed 's/\n/ /g')
	result+=" "
done
echo "$result"
exit
