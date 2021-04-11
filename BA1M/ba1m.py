from sys import stdin
from numpy import base_repr

n = int(stdin.readline().strip())
k = int(stdin.readline().strip())

n = base_repr(n, base=4)

while len(n) < k:
    n = "0" + n 

result = ""

for c in n:
    if c == "0":
        result = result + "A"
    if c == "1":
        result = result + "C"
    if c == "2":
        result = result + "G"
    if c == "3":
        result = result + "T"

print(result)
