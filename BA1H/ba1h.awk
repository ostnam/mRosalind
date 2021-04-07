{
	lines[NR] = $0
}
END {
	pattern = lines[1]
	text    = lines[2]
	max     = lines[3]
	result  = ""

	for (i = 1; i <= length(text) - length(pattern); i++) {
		count = 0
		for (j = 1; j <= length(pattern); j++) {
			if (substr(pattern, j, 1) != substr(text, j+i, 1)) {
				++count
			}
		}
		if (count <= (max + 0)) {
			result = result " " i
		}
	}
	print result
}

