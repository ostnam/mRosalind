def random_motif_search(seqs_list, k, t):
    best_motifs = kmer_random(seqs_list, k)
    current_motifs = best_motifs
    while True:
        profile = motif_matrix(current_motifs)
        current_motifs = [profile_most(profile, i, k) for i in seqs_list]
        if score(current_motifs) < score(best_motifs):
            best_motifs = current_motifs
        else:
            return best_motifs

def motif_matrix(kmer_list):
    """ returns a profile matrix from a list of strings
        the strings must only contain ACGT
    """
    result = list()
    for c in ("A", "C", "G", "T"):
        line = [sum(map(lambda a: a == c, i))+1 for i in zip(*kmer_list)] # list of count
        result.append(line)
    result = [list(map(lambda a: a / len(kmer_list), i)) for i in result]
    return result

def kmer_random(seqs, k):
    """return a list of random kmers of each string in seqs"""
    from random import randrange
    result = list()
    for i in seqs:
        rando = randrange(0, len(i)-k+1)
        result.append(i[rando:rando+k])
    return result 

def kmer_generator(seq, k):
    for i in range(0, len(seq)-k+1):
        yield seq[i:i+k]

def profile_most(motif_matrix, seq, k):
    """returns the highest scoring substring from a motif matrix
       the string must only contain ACGT
    """
    index = {"A": 0, "C": 1, "G":2, "T":3}
    best = -1.0
    best_kmer = ""
    for kmer in kmer_generator(seq, k):
        result = 1
        for (i, char) in enumerate(kmer):
            key = index[char] 
            result *= motif_matrix[key][i]
        if result > best:
            best = result
            best_kmer = kmer
    return best_kmer

def score(motifs):
    """returns the 'score' of a collection of strings
       the score is the sum of the subscore at every char
       the subscore is the number of strings having a different char than the
       most common one at that position in the collection
    """
    from collections import Counter
    result = 0
    for bases in zip(*motifs):
        a = Counter(bases)
        for i in a.most_common()[1:]:
            result += i[1]
    return result


if __name__ == "__main__":
    from sys import stdin
    (k, t) = map(int, stdin.readline().strip().split())
    seqs_list = [l for l in stdin.read().strip().split() if l != ""]
    result = random_motif_search(seqs_list, k, t)
    for i in range(1000):
        mots = random_motif_search(seqs_list, k, t)
        if score(mots) < score(result):
            result = mots
    for i in result:
        print(i)
