from sys import argv
from Bio import SeqIO

begin_match = int(argv[1])-1
end_match = int(argv[2])-1

def count_instances(pat, seq):
    count = 0
    for i in range(len(seq)-len(pat)):
        diff = 0
        substring = seq[i:i+len(pat)+1]
        for (a, b) in zip(pat, substring):
            if a != b: 
                diff += 1
        if diff <= 3:
            count +=1
    return count

with open("rosalind_subo.txt", "r") as f:
    records = [record.seq for record in SeqIO.parse(f, "fasta")]

pattern = records[0][begin_match:end_match]
print(count_instances(pattern, records[0]), count_instances(pattern, records[1]))
