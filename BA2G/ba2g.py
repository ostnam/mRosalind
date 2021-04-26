def gibbs_sampler(seqs_list, k, t, n):
    best_motifs = kmer_random(seqs_list, k)
    current_motifs = best_motifs
    for j in range(n): 
        i = randrange(0, t)                         
        current_motifs = [p for (ind, p) in enumerate(current_motifs) if ind != i] # motifs with the i-th motif removed
        profile = motif_matrix(current_motifs)                                     # build profile matrix without selected motif
        current_motifs.insert(i, random_kmer_with_profile(seqs_list[i], k, profile))
        if score(current_motifs) < score(best_motifs):
            best_motifs = current_motifs
    return best_motifs

def kmer_random(seqs, k):
    """return a list of random kmers of each string in seqs"""
    result = list()
    for i in seqs:
        rando = randrange(0, len(i)-k+1)
        result.append(i[rando:rando+k])
    return result 

def random_kmer_with_profile(seq, k, profile):
    """return a random kmer according to Gibbs sampling"""
    all_kmers = list(kmer_generator(seq, k)) # collect every kmer in a list
    all_kmers_with_prob = {i: kmer_prob(i, profile) for i in all_kmers}
    total_prob = sum(all_kmers_with_prob.values())
    point = uniform(0, total_prob)
    position = 0.0
    for (kmer, prob) in all_kmers_with_prob.items():
        if position < point:
            position += prob
            if position > point:
                return kmer
        else:
            break
    return kmer


def kmer_prob(kmer, profile):
    """returns the probability of a kmer according to a profile matrix
    """
    result = 1.0
    indices = {"A": 0, "C": 1, "G":2, "T":3}
    for (index, char) in enumerate(kmer):
        key = indices[char]
        result *= profile[key][index]
    return result

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

def kmer_generator(seq, k):
    for i in range(0, len(seq)-k+1):
        yield seq[i:i+k]

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
    from random import randrange, uniform
    (k, t, n) = map(int, stdin.readline().strip().split())
    seqs_list = [l for l in stdin.read().strip().split() if l != ""]
    result = gibbs_sampler(seqs_list, k, t, n)
    for i in range(20):
        mots = gibbs_sampler(seqs_list, k, t, n)
        if score(mots) < score(result):
            result = mots
    for i in result:
        print(i)
