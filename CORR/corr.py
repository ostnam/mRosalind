from Bio import SeqIO
seqs = [str(rec.seq) for rec in SeqIO.parse("rosalind_corr.txt", "fasta")]
correct = set()
incorrect = set()

def rev_comp(sequence):
    comp = sequence[::-1]
    comp = comp.replace("A", "B")
    comp = comp.replace("T", "A")
    comp = comp.replace("B", "T")
    comp = comp.replace("C", "D")
    comp = comp.replace("G", "C")
    comp = comp.replace("D", "G")
    return comp

for seq in seqs:
    rev = rev_comp(seq)
    if seq in correct or rev in correct:
        continue
    elif seq in incorrect or rev in incorrect:
        incorrect.discard(seq)
        incorrect.discard(rev)
        correct.add(seq)
    else:
        incorrect.add(seq)

for seq in incorrect:
    for seq2 in correct:
        for base in (seq2, rev_comp(seq2)):
            num_diff = 0
            for i in zip(seq, base):
                if i[0] != i[1]:
                    num_diff += 1
                if num_diff > 1:
                    break
            if num_diff <= 1:
                print(seq, "->", base, sep="")
