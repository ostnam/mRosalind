from sys import stdin
k = int(stdin.readline().strip())
text = stdin.readline().strip()
kmers = {text[i:i+k-1] for i in range(len(text)-k+2)}
result = dict()
for i in kmers:
    current = set()
    for j in kmers:
        if i[1:] == j[:-1]:
            current.add(j)
    if len(current) != 0:
        result[i] = current

for (key, val) in result.items():
    if len(val) == 1:
        print(key, "->", val.pop(), end="")
    else:
        print(key, "->", end=" ")
        first = True
        for i in val:
            if not first:
                print(",", end="")
            if first:
                first = False
            print(i, end="")
    print()



edges = {i[1:] for i in kmers for j in kmers if i[1:] == j[:-1]}
