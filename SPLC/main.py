from Bio import SeqIO
seqs = [str(rec.seq) for rec in SeqIO.parse("raw.fasta", "fasta")]
# Reads the FASTA files and assigns each sequence to the list seqs

sequence = seqs[0]
del seqs[0]
# Separates the main sequence to the "sequence" string, and deletes it from the intron list

x = 0
for x in range(0, len(seqs)):
	sequence = sequence.replace(seqs[x], "")
# For each sequence in seqs, delete it from sequence	


from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

coding_dna = Seq(sequence, IUPAC.unambiguous_dna)
peptide = str(coding_dna.translate())
#puts the sequence string into a coding dna thingie for biopython, which then translates it into the "peptide" string

print(peptide, file=open("peptide2.txt", "w"))
print("Your sequence has been translated into the peptide2.txt file")
