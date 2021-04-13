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
    (d, ) = tuple(map(int, stdin.readline().strip().split()))

    kmer_dict = dict(map(lambda a: ("".join(a), 0), product(("A", "T", "G", "C"), repeat=len(string))))
    # dict of 0 for every kmer
    for i in kmer_dict:
        if approx_match(string, i, d):
            print(i)
