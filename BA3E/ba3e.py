from sys import stdin
kmers = [i.strip() for i in stdin]
result = {i[:-1]: [] for i in kmers}
for i in kmers:
    result[i[:-1]].append(i[1:])

for (key, val) in result.items():
    if len(val) == 0:
        continue
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
