def motif_matrix(kmer_list):
    """ returns a profile matrix from a list of strings
        the strings must only contain ACGT
    """
    result = list()
    for c in ("A", "C", "G", "T"):
        line = [sum(map(lambda a: a == c, i)) for i in zip(*kmer_list)] # list of count
        result.append(line)
    result = [list(map(lambda a: a / len(kmer_list), i)) for i in result]
    return result

def kmer_generator(seq, k):
    """yields every substring of length k from seq"""
    for i in range(len(seq) - k + 1):
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

def greedy_motif_search(seqs_list, k, t):
    first_kmers = [i[0:k] for i in seqs_list]
    best_motifs = first_kmers 
    for motif1 in kmer_generator(seqs_list[0], k): # for each kmer in string 0
        curr_motif = [motif1]
        for i in range(1, t):
            profile = motif_matrix(curr_motif)
            curr_motif.append(profile_most(profile, seqs_list[i], k))
        if score(curr_motif) < score(best_motifs):
            best_motifs = curr_motif
    return best_motifs


if __name__ == "__main__":
    from sys import stdin
    (k, t) = map(int, stdin.readline().strip().split())
    seqs_list = [l for l in stdin.read().strip().split() if l != ""]
    result = greedy_motif_search(seqs_list, k, t)
    for i in result:
        print(i)
