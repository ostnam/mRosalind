sequences = []
with open("rosalind_pdst.txt", "r") as f:
    current = ""
    while True:
        if (l := f.readline()).startswith(">"):
            if current != "":
                sequences.append(current)
            current = ""
        elif l == "":
            sequences.append(current)
            break
        else:
            current += l.strip()

for i in sequences:
    for j in sequences:
        count = 0
        for (a, b) in zip(i, j):
            if a != b:
                count += 1
        print("%.5f" % (count/len(i)), end=" ")
    print("")
