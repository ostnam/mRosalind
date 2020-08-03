### 1: Turning the FASTA file into a sequence string
from Bio import SeqIO
seqs = [str(rec.seq) for rec in SeqIO.parse("raw.fasta", "fasta")]
# Reads the FASTA files and assigns the sequence string to the "seqs" list

sequence = seqs[0]
# Separates the main sequence to the "sequence" string
# probably should be deleted

### 2: Obtaining the reverse complement string of that string
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
coding_dna1 = Seq(sequence, IUPAC.unambiguous_dna)
# Turns the sequence string into a biopython sequence object, necessary to obtain its reverse complement and later translate it

reverse_complement = str(coding_dna1.reverse_complement())
# Obtains the RC string

### 3: Obtaining the extras ORFs
ORF2 = sequence[1:]
ORF3 = sequence[2:]
ORF5 = reverse_complement[1:]
ORF6 = reverse_complement[2:]
# Creates the 4 last ORF by shifting the reading frame by one or two nucleotides

seqs.append(ORF2)
seqs.append(ORF3)
seqs.append(reverse_complement)
seqs.append(ORF5)
seqs.append(ORF6)
# Adds the 5 additional ORF to the "seqs" list

### 4: Translating each ORF into its corresponding peptide string and putting it into a list
protseqs = list() 
protseqs_valid = list()
protseqs_raw = list()
results = list()

for i in range(len(seqs)):
	coding_dna = Seq(seqs[i], IUPAC.unambiguous_dna)
	peptide = str(coding_dna.translate())
	protseqs_raw.append(peptide)
# Produces a raw translated string list: protseqs_raw, from the raw ORFs

for i in range(len(protseqs_raw)):
		if ("M" in protseqs_raw[i]) and ("*" in protseqs_raw[i]):
			protseqs_valid.append(protseqs_raw[i])
# Extracts all the strings with a start and stop codon from the previous list and puts them in the protseqs_valid list
# that step might be useless

for i in range(len(protseqs_valid)):
	working_seq = str(protseqs_valid[i])
	start_codons =  working_seq.count("M")
	for x in range(start_codons):
		start_position = working_seq.index("M")
		seqstring = working_seq[start_position:]
		if "*" in seqstring:
			protseqs.append(seqstring)
		working_seq = seqstring[1:]
# Separates each string starting from each possible start codon and puts them all in the protseqs list if they contain a stop codon

for i in range(len(protseqs)):
	working_seq = str(protseqs[i])
	if "*" in working_seq:
		stop_position = working_seq.index("*")
		results.append(working_seq[:stop_position])
# Cuts each of the possible sequences at the first codon

r = set(results)
results = list(r)
# Removes duplicates from the results

results_string = ""
for i in range(len(results)):
	results_string = results_string + results[i] + "\n"
# Creates a results strings countaining each peptide sequence separated by a new line

print(results_string, file=open("results.txt", "w"))
