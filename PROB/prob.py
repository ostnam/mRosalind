from math import log

def prob(seq, gc):
    prob = 0
    for char in seq:
        if char in ("G", "C"):
            prob += log(gc/2, 10)
        else:
            prob += log((1-gc)/2, 10)
    return prob

with open("rosalind_prob.txt", "r") as f:
    seq = f.readline().strip()
    A = list(map(float, f.readline().split(" ")))

for k in A:
    print(f"{prob(seq, k):.3f}", end=" ")
print("")
