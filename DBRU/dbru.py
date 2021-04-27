from sys import stdin

def reverse_complement(string):
    string = string[::-1]
    string = string.replace("A", "1")
    string = string.replace("T", "A")
    string = string.replace("1", "T")
    string = string.replace("G", "1")
    string = string.replace("C", "G")
    string = string.replace("1", "C")
    return string

kmers = {i.strip() for i in stdin}
temp = set()
for i in kmers:
    temp.add(reverse_complement(i))
kmers = kmers.union(temp)

result = set()
for i in kmers:
    result.add((i[:-1], i[1:]))

for i in result:
    print("(" + i[0] + ", " + i[1] + ")")
