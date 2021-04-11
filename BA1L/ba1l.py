import sys

p = sys.stdin.readline()
base_4 = ""
for c in p:
    if   c == 'A':
        base_4 = base_4 + '0'
    elif c == 'C':
        base_4 = base_4 + '1'
    elif c == 'G':
        base_4 = base_4 + '2'
    elif c == 'T':
        base_4 = base_4 + '3'

print(int(base_4, 4))
