# the inputs are taken from positional argument
# exemple of use: "cat rosalind_afrq.py | xargs python3 afrq.py"
from sys import argv
from math import sqrt

def B(k):
    q = sqrt(k)
    p = 1-sqrt(k)
    return 2*p*q+k

for i in argv[1:]:
    print("%.3f" % B(float(i)), end=" ")
print("")
