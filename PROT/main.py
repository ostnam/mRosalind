try:
    rawtxt = open("raw.txt")
    raw = rawtxt.read()
    rawtxt.close()
except:
    print("The program couldn't launch, probably because you didn't put a correct file in the directory of the program.")

raw = raw.replace(" ", "")
raw = raw.replace("\n", "")

basepair = 0
peptide = ""

while basepair < len(raw):
	codon = raw[basepair:basepair+3]
	if (codon == "UUU") or (codon == "UUC"):
		peptide = peptide + "F"
	elif (codon == "UUA") or (codon == "UUG"):
		peptide = peptide + "L"
	elif (codon == "UCU") or (codon == "UCC") or (codon == "UCA") or (codon == "UCG"):
		peptide = peptide + "S"
	elif (codon == "UAU") or (codon == "UAC"):
		peptide = peptide + "Y"
	elif (codon == "UAA") or (codon == "UAG") or (codon == "UGA"):
		peptide = peptide + ""
	elif (codon == "UGU") or (codon == "UGC"):
		peptide = peptide + "C"
	elif (codon == "UGG"):
		peptide = peptide + "W"
	elif (codon == "CUU") or (codon == "CUC") or (codon == "CUA") or (codon == "CUG"):
		peptide = peptide + "L"
	elif (codon == "CCU") or (codon == "CCC") or (codon == "CCA") or (codon == "CCG"):
		peptide = peptide + "P"
	elif (codon == "CAU") or (codon == "CAC"):
		peptide = peptide + "H"
	elif (codon == "CAA") or (codon == "CAG"):
		peptide = peptide + "Q"
	elif (codon == "CGU") or (codon == "CGC") or (codon == "CGA") or (codon == "CGG"):
		peptide = peptide + "R"
	elif (codon == "AUU") or (codon == "AUC") or (codon == "AUA"):
		peptide = peptide + "I"
	elif (codon == "AUG"):
		peptide = peptide + "M"
	elif (codon == "ACU") or (codon == "ACC") or (codon == "ACA") or (codon == "ACG"):
		peptide = peptide + "T"
	elif (codon == "AAU") or (codon == "AAC"):
		peptide = peptide + "N"
	elif (codon == "AAA") or (codon == "AAG"):
		peptide = peptide + "K"
	elif (codon == "AGU") or (codon == "AGC"):
		peptide = peptide + "S"
	elif (codon == "AGA") or (codon == "AGG"):
		peptide = peptide + "R"
	elif (codon == "GUU") or (codon == "GUC") or (codon == "GUA") or (codon == "GUG"):
		peptide = peptide + "V"
	elif (codon == "GCU") or (codon == "GCC") or (codon == "GCA") or (codon == "GCG"):
		peptide = peptide + "A"
	elif (codon == "GAU") or (codon == "GAC"):
		peptide = peptide + "D"
	elif (codon == "GAA") or (codon == "GAG"):
		peptide = peptide + "E"
	elif (codon == "GGU") or (codon == "GGC") or (codon == "GGA") or (codon == "GGG"):
		peptide = peptide + "G"
	basepair = basepair + 3

print(peptide, file=open("peptide.txt", "w"))
