# Rosalind DNA
dna = str(input("Paste the DNA string here: \n"))

adenine = dna.count("A")
thymine = dna.count("T")
guanine = dna.count("G")
cytosine = dna.count("C")

count_dict = {"A": adenine, "T": thymine, "G": guanine, "C": cytosine}

print(count_dict)
