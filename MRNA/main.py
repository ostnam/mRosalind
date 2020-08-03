try:
    rawtxt = open("raw.txt")
    raw = rawtxt.read()
    rawtxt.close()
except:
    print("The program couldn't launch, probably because you didn't put a correct file in the directory of the program.")

raw = raw.replace(" ", "")
raw = raw.replace("\n", "")

possibilities = 3
aminoacid = 0

while aminoacid < len(raw):
	x = raw[aminoacid]
	if (x == "L") or (x == "R") or (x == "S"):
		possibilities = possibilities * 6
	if (x == "P") or (x == "T") or (x == "V") or (x == "A") or (x == "G"):
		possibilities = possibilities * 4
	elif (x == "I"):
		possibilities = possibilities * 3
	elif (x == "F") or (x == "H") or (x == "Y") or (x == "C") or (x == "Q") or (x == "N") or (x == "K") or (x == "D") or (x == "E"):
		possibilities = possibilities * 2
	aminoacid = aminoacid + 1

print(possibilities % 1000000)
