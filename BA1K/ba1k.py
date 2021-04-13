from sys import stdin
from itertools import product
string = stdin.readline().strip()
(k, ) = tuple(map(int, stdin.readline().strip().split()))

kmer_dict = dict(map(lambda a: ("".join(a), 0), product(("A", "C", "G", "T"), repeat=k)))
# dict of 0 for every kmer

for i in range(len(string)-k+1):
    substr = string[i:i+k]
    for kmer in kmer_dict:
        if substr == kmer:
            kmer_dict[kmer] += 1

for i in kmer_dict:
    print(kmer_dict[i], end=" ")
print()

