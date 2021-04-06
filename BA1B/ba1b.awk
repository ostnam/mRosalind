#!/bin/awk -f
BEGIN {
}
{
	lines[NR] = $0
}
END {
	k = lines[NR]
	dna_str = ""
	for (i = 0; i < NR; i++) {
		dna_str = dna_str lines[i]
	}
	for (i = 1; i <= length(dna_str) - k + 1; i++) {
		++kmers[substr(dna_str, i, k)]
	}
	
	max_set = 0
	max_arr[""] = 0
	max_arr_len = 0
	for (kmer in kmers) {
		if (kmers[kmer] > max_set) {
			max_set = kmers[kmer]
			delete max_arr
			max_arr_len = 0
			max_arr[max_arr_len] = kmer
			++max_arr_len
			continue
		}
		if (kmers[kmer] == max_set) {
			max_arr[max_arr_len] = kmer
			++max_arr_len
		}
	}
	for (i in max_arr) {
		printf("%s ", max_arr[i])
	}
	printf("\n")
}
