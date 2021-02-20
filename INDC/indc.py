from math import log
from scipy.stats import binom

with open("rosalind_indc.txt", "r") as f:
    n = int(f.readline().strip())

for i in range(2*n):
    x = log(binom(2*n, 0.5).sf(i), 10)
    print("%.3f" % x, end=" ")

print("")
