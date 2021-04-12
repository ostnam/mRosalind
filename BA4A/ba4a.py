from Bio.Seq import translate
from sys import stdin

seq = stdin.readline()
print(translate(seq).replace("*", ""))
