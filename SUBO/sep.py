from Bio import SeqIO

with open("rosalind_subo.txt", "r") as f:
    records = [record for record in SeqIO.parse(f, "fasta")]

SeqIO.write(records[0], "pattern1", "fasta")
SeqIO.write(records[1], "pattern2", "fasta")
