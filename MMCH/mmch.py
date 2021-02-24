from sys import argv

def max_match(a, b):
    count=1
    while min(a, b) > 0:
        count = count*max(a, b)
        a-=1
        b-=1
    return count

A_count = int(argv[1])
C_count = int(argv[2])
G_count = int(argv[3])
U_count = int(argv[4])
print(max_match(A_count, U_count)*max_match(C_count, G_count))
