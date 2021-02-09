from Bio import SeqIO
with open("rosalind_phre.txt", "r") as f:
    n = int(f.readline())
    qualities = []
    for record in SeqIO.parse(f, "fastq"):
        qualities.append(record.letter_annotations["phred_quality"])

average = [sum(i)/len(i) for i in qualities]
print(len(list(filter(lambda a: a <=n, average))))
