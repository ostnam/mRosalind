from Bio import SeqIO

with open("rosalind_bfil.txt", "r") as f:
    q = int(f.readline())
    records = [record for record in SeqIO.parse(f, "fastq")]

resulting_records = []

for record in records:
    beginning_cutoff = 0
    while record.letter_annotations["phred_quality"][beginning_cutoff] < q:
        beginning_cutoff += 1
    end_cutoff = len(record.seq)
    while record.letter_annotations["phred_quality"][end_cutoff-1] < q:
        end_cutoff -= 1
    new_record = record[beginning_cutoff:end_cutoff]
    resulting_records.append(new_record)

SeqIO.write(resulting_records, "result", "fastq")
