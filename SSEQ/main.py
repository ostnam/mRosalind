### 1: Turning the FASTA file into a sequence string
from Bio import SeqIO
seqs = [str(rec.seq) for rec in SeqIO.parse("raw.fasta", "fasta")]
# Reads the FASTA files and assigns the sequence string to the "seqs" list

sequence = seqs[0]
subsequence = seqs[1]
# Separates the main sequence to the "sequence" string

results = list()
x = 0
for i in range (len(sequence)):
	working_base = subsequence[x]
	if working_base == sequence[i]:
		results.append(i+1)
		x = x + 1
	if x == len(subsequence):
		break

results_string = ""
for i in range(len(results)):
	results_string = results_string + str(results[i])
	results_string = results_string + " "

print(results_string, file=open("results.txt", "w"))
