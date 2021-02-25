from itertools import combinations
x = list(filter(lambda a: a[1] > a[0] + 1, combinations(range(11), 2)))
res = ""
for i in x:
        res = res + str(i[0]) + " " + str(i[1]) + "\n"

with open("permutations.txt", "w") as f:
    f.write(res)
