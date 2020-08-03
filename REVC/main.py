# Rosalind 3
try:
    dnatxt = open("dna.txt")
    dna = dnatxt.read()
    dnatxt.close()
except:
    print("The program couldn't launch, probably because you didn't put a dna.txt file in the directory of the program.")

comp = dna[::-1]
comp = comp.replace("A", "B")
comp = comp.replace("T", "A")
comp = comp.replace("B", "T")
comp = comp.replace("C", "D")
comp = comp.replace("G", "C")
comp = comp.replace("D", "G")
print(comp, file=open("comp.txt", "w"))
