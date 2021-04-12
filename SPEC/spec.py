from sys import stdin

def float_equal(a, b):
    """since we can't trust == with floats"""
    # I used this in a previous approach but it's not used in the final version
    return (a * 1.0002 > b) and (b * 1.0002 > a)

def find_smallest_ratio():
    """I used this to find the correct sensitivity for float equal"""
    # not used in the final version either
    smallest = 0.0
    for i in rev_table:
        for j in rev_table:
            if i < j:
                if smallest < i/j:
                    smallest = i/j
    print(smallest)

table = { "A":    71.03711,
          "C":   103.00919,
          "D":   115.02694,
          "E":   129.04259,
          "F":   147.06841,
          "G":    57.02146,
          "H":   137.05891,
          "I":   113.08406,
          "K":   128.09496,
          "L":   113.08406,
          "M":   131.04049,
          "N":   114.04293,
          "P":    97.05276,
          "Q":   128.05858,
          "R":   156.10111,
          "S":    87.03203,
          "T":   101.04768,
          "V":    99.06841,
          "W":   186.07931,
          "Y":   163.06333,
          }

rev_table = dict(map(lambda a: (a[1], a[0]), table.items())) # dict of weight: residue

if __name__ == "__main__":
    l = list(map(float, stdin.read().split())) # input
    n = len(l)-1
    
    diffs = list()
    for i in range(n, 0, -1):
        diffs.append(l[i]-l[i-1])
    # builds a list of the difference
    result = ""
    for i in reversed(diffs):
        closest = 10
        aa_to_add = ""
        for j in rev_table:
            if abs(i-j) < closest:
                closest = abs(i-j)
                aa_to_add = rev_table[j]
        result = result + aa_to_add

    print(result)
