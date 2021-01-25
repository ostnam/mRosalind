### My solution to the rosalind SIGN problem
### Run it with n as the first positional argument (eg python3 sign.py 2)
import itertools
import math
import sys

def list_of_permutations(n):
    """Returns a list of every permutations of the ints between 1 and n included"""    
    return list(itertools.permutations([k for k in range(1, n+1)]))

def number_of_signed_permutations(n):
    return math.factorial(n)*2**n

def get_signs_permutations(length):
    """Returns every possible sign combination of a length"""
    return list(itertools.product([-1, 1], repeat=length))

if __name__ == "__main__":
    n = int(sys.argv[1])
    signs_permutations = get_signs_permutations(n)
    unsigned_permutations = list_of_permutations(n)
    result = [ [x*j[index] for (index, x) in enumerate(i)] for i in unsigned_permutations for j in signs_permutations ]

    print(number_of_signed_permutations(n))
    for i in result:
        print(*i, sep=" ")
