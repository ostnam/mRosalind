# this takes a while to run, but can be finished in around 4 minutes with pypy3 (python3 is slightly slower)
from itertools import combinations

def reversal_distance(a, b):
    seen_before = {a: 0}
    distance = 0
    permut_keys = list(combinations(range(11), 2))
    while b not in seen_before:
        distance += 1
        added_last_cycle = [k for k, v in seen_before.items() if v == distance - 1]
        for old in added_last_cycle:
            for j in permut_keys:
                if j[0] == j[1] + 1:
                    continue
                new = permut_list_new(old, j)
                if new == b:
                    return distance
                if new not in seen_before:
                    seen_before[new] = distance
    return seen_before[b]

def permut_list_new(l, keys):
    a = l[:keys[0]] + l[keys[0]:keys[1]][::-1] + l[keys[1]:]
    return a 

if __name__ == "__main__":
    collection = []
    with open("rosalind_rear.txt", "r") as f:
        while True: 
            a = f.readline()
            if a == "":
                break
            if a.strip() == "":
                continue
            else:
                a = "".join(map(lambda a: str(int(a)-1), a.strip().split(" ")))
                b = "".join(map(lambda a: str(int(a)-1), f.readline().strip().split(" ")))
                collection.append([a, b])
    for pair in collection:
        print(reversal_distance(pair[0], pair[1]), end=" ")
    print("")
