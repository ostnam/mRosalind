from Bio import SeqIO
k = 3
result = set()
def verify_match(sequence_a, sequence_b, k):
    slice_a = sequence_a[-k:]
    slice_b = sequence_b[:k]
    return (slice_a == slice_b)

sequences = [record for record in SeqIO.parse("rosalind_grph.txt", "fasta")]

for i in sequences:
    for j in sequences:
        if i.id == j.id: continue
        if verify_match(i.seq, j.seq, k) == True:
           result.add( (i.id, j.id) )

for entry in result:
    print(entry[0], entry[1])

