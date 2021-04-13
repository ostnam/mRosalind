def approx_match(a, b, d):
    count = 0
    for (x, y) in zip(a, b):
        if x != y:
            count += 1
            if count > d:
                return False
    return True

if __name__ == "__main__":
    from sys import stdin
    from itertools import product
    string = stdin.readline().strip()
    (k, d) = tuple(map(int, stdin.readline().strip().split()))

    kmer_dict = dict(map(lambda a: ("".join(a), 0), product(("A", "T", "G", "C"), repeat=k)))
    # dict of 0 for every kmer
    
    maxima      = 0
    maxima_list = list()

    for i in range(len(string)-k+1):
        substr = string[i:i+k]
        for kmer in kmer_dict:
            if approx_match(substr, kmer, d):
                kmer_dict[kmer] += 1
                if kmer_dict[kmer] > maxima:
                    maxima_list.clear()
                    maxima_list.append(kmer)
                    maxima = kmer_dict[kmer]
                elif kmer_dict[kmer] == maxima:
                    maxima_list.append(kmer)

    for i in maxima_list:
        print(i, end=" ")
    print()

