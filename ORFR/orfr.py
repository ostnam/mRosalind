from Bio import Seq
with open("rosalind_orfr.txt") as f:
    S = f.read().strip()

S = Seq.Seq(S)
longest_string = ""
for i in range(3):
    for a in (S, S.reverse_complement()):
        for protein in a[i:].translate().split("*"):
            beginning = protein.find("M")
            final_protein = protein[beginning:]
            if len(final_protein) > len(longest_string):
                longest_string = final_protein

print(longest_string)
