from sys import stdin
import pandas as pd

path = stdin.readline().strip()
stdin.readline() # throwing away separator lines
states = stdin.readline().strip().split()
stdin.readline()

df = pd.read_csv(stdin, sep="\s", engine="python")
result = 1.0/len(states) # initial probabilities are equal

for (i, c) in enumerate(path):
    if i == len(path) - 1:
        break
    else:
        result *= float(df[path[i+1]][c])

print(result)
