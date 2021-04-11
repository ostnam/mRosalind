# "The genotype frequencies at equilibrium are p and q for the heterogametic sex but p^2, 2pq and q^2 for the homogametic sex."
#       - Wikipedia
# A[k] = p : probability that a male has a recessive allele
# q = 1-p
# B[k] : probability that a female has 1 recessive allele = 2pq
# => B[k] = 2*( A[k] * (1-A[k]) )
#           2*   p   * (   q  )

from sys import stdin
A = list(map(float, stdin.readline().strip().split()))
for i in A:
    print((2*(i*(1-i))), end=" ")
print()
