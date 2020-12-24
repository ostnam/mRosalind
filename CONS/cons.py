from Bio import SeqIO
def vertical_strings_array(array):
    vertical_array = [""] * len(array[0])
    for i in range(len(array[0])):
        for j in array:
            vertical_array[i] += j[i]
    return vertical_array

def highest_key(**kwargs):
    highest = max(kwargs.values())
    for i in kwargs:
        if kwargs[i] == highest: 
            return i

if __name__ == "__main__":
    sequences = [str(record.seq) for record in SeqIO.parse("rosalind_cons.txt", "fasta")]
    bases = ["A", "C", "G", "T"]

    vertical_strings = vertical_strings_array(sequences)
    matrix = {i: [j.count(i) for j in vertical_strings] for i in bases}
    consensus_string = ""
    for i in range(len(matrix["A"])):
        count = {base: matrix[base][i] for base in matrix}
        consensus_string += highest_key(**count)


    print(consensus_string, end="")
    for base in bases:
        print("\n", end="")
        print(base + ":", end ="")
        for i in matrix[base]:
            print(" " + str(i), end="")
