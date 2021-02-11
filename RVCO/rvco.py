from Bio import SeqIO

with open("rosalind_rvco.txt", "r") as f:
    records = list(SeqIO.parse(f, "fasta").records)

result = 0
for record in records:
    if (record.reverse_complement().seq == record.seq):
        result += 1

print(result)
