import re
from itertools import product
from Bio import SeqIO

def get_index(i):
    result = ""
    for char in i:
        result += hex(letter_list.index(char))
    return result

sequences = [str(rec.seq) for rec in SeqIO.parse("rosalind_kmer.txt", "fasta")]
letter_list = ["A", "C", "G", "T"]
permutations_array = []
[permutations_array.append("".join(j)) for j in product(letter_list, repeat=4)]
permutations_array.sort(key=get_index)

for kmer in permutations_array:
    print(len(re.findall("(?=" + kmer + ")", sequences[0])), end=" ")
