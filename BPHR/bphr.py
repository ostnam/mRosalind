from Bio import SeqIO

with open("rosalind_bphr.txt", "r") as f:
    q = int(f.readline())
    qualities = []
    for record in SeqIO.parse(f, "fastq"):
        qualities.append(record.letter_annotations["phred_quality"])

count = 0
for i in range(len(qualities[0])):
    total = 0
    for j in qualities:
        total += j[i]
    mean = total / len(qualities)
    if mean < q:
        count += 1

print(count)
