def delta_func(a, b):
    if a == b:
        return 0
    return 1

def edit_distance_table(a, b):
    # building the table
    result = list()
    for i in range(len(a)+1):
        result.append(list())
        for j in range(len(b)+1):
            result[i].append(0)
    # initializing values
    for i in range(len(a)+1):
        result[i][0] = i
    for i in range(len(b)+1):
        result[0][i] = i
    # filling the table
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            delta = delta_func(a[i-1], b[j-1])
            minima = min(result[i-1][j-1] + delta,
                         result[i-1][j] + 1,
                         result[i][j-1] + 1)
            result[i][j] = minima
    return result

def create_aligns(table, a, b):
    """
    same approach as the edit distance problem
    but the table will store the number of ways of reaching each cell
    """
    result = list()
    for i in range(len(a)+1):
        result.append(list())
        for j in range(len(b)+1):
            result[i].append(0)
    # initializing values
    # only 1 way of filling the first row/column: going straight right/down
    for i in range(len(a)+1):
        result[i][0] = 1
    for i in range(len(b)+1):
        result[0][i] = 1

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            delta = delta_func(a[i-1], b[j-1])
            minima = min(table[i-1][j-1] + delta,
                         table[i-1][j] + 1,
                         table[i][j-1] + 1)
            if table[i-1][j-1] + delta == minima:
                result[i][j] += result[i-1][j-1]
            if table[i-1][j] + 1 == minima:
                result[i][j] += result[i-1][j]
            if table[i][j-1] + 1 == minima:
                result[i][j] += result[i][j-1]
            # the number of ways to reach a cell C is the sum of the number of ways you can reach each cells that can reach C

    return(result[i][j])

if __name__ == "__main__":
    # parsing input into strings a and b
    from sys import stdin

    stdin.readline()
    a = ""
    while (not (i:=stdin.readline()).startswith(">")):
        a = a + i.strip()

    b = ""
    while ( (i:=stdin.readline().strip()) != ""):
        b = b + i

    table = edit_distance_table(a, b)
    print(create_aligns(table, a, b) % 134217727)
