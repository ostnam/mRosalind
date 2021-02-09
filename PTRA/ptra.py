from Bio.Seq import translate
with open("rosalind_ptra.txt", "r") as f:
    seq = f.readline().replace("\n", "")
    res = f.readline().replace("\n", "")
for i in range(1, 16):
    if translate(seq, table=i) == res + "*":
        print(i)
        break
