def expected(string, n, gc):
    if gc in (0.000, 1.000):
        return 0.000
    positions = n - (len(string) - 1)
    prob = 1
    for i in string:
        if i in ("G", "C"):
            prob *= gc * 0.5
        elif i in ("A", "T"):
            prob *= (1-gc) * 0.5
    return positions * prob

if __name__ == "__main__":
    with open("rosalind_eval.txt", "r") as f:
        n = int(f.readline())
        s = f.readline().strip()
        A = list(map(lambda a: float(a), f.readline().strip().split()))

    for i in A:
        print("%.3f" % expected(s, n, i), end=" ")
