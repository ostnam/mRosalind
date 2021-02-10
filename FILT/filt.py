from Bio import SeqIO

with open("rosalind_filt.txt", "r") as f:
    line1 = f.readline()
    (q, p) = line1.split(" ")
    (q, p) = (int(q), int(p))
    qualities = []
    for record in SeqIO.parse(f, "fastq"):
        qualities.append(record.letter_annotations["phred_quality"])

percents_that_passes = []
for i in qualities:
    count = 0
    for a in i:
        if a >= q:
            count += 1
    percent_in_i = count / len(i)
    percents_that_passes.append(percent_in_i)

result = 0
for i in percents_that_passes:
    if i >= p/100:
        result += 1

print(result)
