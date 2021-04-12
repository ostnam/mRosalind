{
	input[NR] = $0
}
END {
	k = input[1]
	text = input[2]
	for (i = 1; i <= length(text) - (k - 1); i++) {
		++arr[substr(text, i, k)]
	}
	for (i in arr) {
		print i
	}
}
