def delta_func(a, b):
    return -df[a][b]

def edit_distance_table(a, b):
    # building the table
    result = list()
    for i in range(len(a)+1):
        result.append(list())
        for j in range(len(b)+1):
            result[i].append(0)
    # initializing values, *5 because gap value is 5
    for i in range(len(a)+1):
        result[i][0] = i*5
    for i in range(len(b)+1):
        result[0][i] = i*5
    # filling the table
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            delta = delta_func(a[i-1], b[j-1])
            minima = min(result[i-1][j-1] + delta,
                         result[i-1][j] + 5,
                         result[i][j-1] + 5)
            result[i][j] = minima
    return result

if __name__ == "__main__":
    # parsing input into strings a and b
    from sys import stdin
    import pandas as pd

    stdin.readline()
    a = ""
    while (not (i:=stdin.readline()).startswith(">")):
        a = a + i.strip()

    b = ""
    while ( (i:=stdin.readline().strip()) != ""):
        b = b + i

    # parsing blosum62
    df = pd.read_csv("blosum62.txt", sep="\s+")

    table = edit_distance_table(a, b)
    print(-table[len(a)][len(b)])
