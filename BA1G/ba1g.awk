#!/bin/awk -f
{
	lines[NR] = $0
}
END {
	count = 0
	for (i = 1; i<=length(lines[1]); i++) {
		char_1 = substr(lines[1], i, 1)
		char_2 = substr(lines[2], i, 1)
		if (char_1 != char_2) {
			++count
		}
	}
	print count
}
