from itertools import product 

def get_index(i):
    result = ""
    for c in i:
        result += hex(letter_list.index(c))
    return result

file1 = open('rosalind_lexv.txt', 'r')
letter_string = file1.readline()
n = int(file1.readline())
letter_list = list(letter_string.split())
permutations_array = []

for i in range(1, n+1):
    [permutations_array.append("".join(j)) for j in product(letter_list, repeat=i)]
permutations_array.sort(key=get_index)

for i in permutations_array:
    print(i)
