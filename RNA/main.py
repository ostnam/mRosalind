# Rosalind 2
try:
    dnatxt = open("dna.txt")
    dna = dnatxt.read()
    dnatxt.close()
except:
    print("The program couldn't launch, probably because you didn't put a dna.txt file in the directory of the program.")

rna = dna.replace("T", "U")
print(rna, file=open("rna.txt", "w"))
