import sys
raw = sys.stdin.read()
results = []
for i in range(len(raw)-3):
    if raw[i] == "N":
        if raw[i+1] != "P":
            if raw[i+2] in ("S", "T"):
                if raw[i+3] != "P":
                    results.append(i)

[sys.stdout.write(str(x) + " ") for x in results]
