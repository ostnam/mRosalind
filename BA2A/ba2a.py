from itertools import product
from functools import reduce
from sys import stdin

def approx_match(a, b, d):
    """returns true if the hamming distance of a to b is equal or less than d"""
    count = 0
    for (i, j) in zip(a, b):
        if i != j:
            count += 1
            if count > d:
                return False
    return True

class Sequence():
    def __init__(self, string):
        self.string = string

    def kmers(self, k):
        """Will yield every kmer of length k"""
        for i in range(len(self.string)-k+1):
            yield self.string[i:i+k]

    def k_d_motifs(self, k, d):
        """return a set of every (k, d)-motifs of self"""
        """that means every kmer of length d that appears in self.string with at most d mismatch"""
        result = set()
        for i in self.kmers(k):
            for j in list(map(lambda a: "".join(a), product(("A", "C", "G", "T"), repeat=k))):
                if approx_match(i, j, d):
                    result.add(j)
        return result

### reading input ###
(k, d) = tuple(map(int, stdin.readline().split()))

dna = list()
while (i := stdin.readline()) != "":
    dna.append(Sequence(i))

### building k_d-motifs set of each string
sets = list()
for seq in dna:
    sets.append(seq.k_d_motifs(k, d))

### build the set of sets elements present in every set and print them
final = set(reduce(lambda a, b: a & b, sets))
for i in final:
    print(i)
