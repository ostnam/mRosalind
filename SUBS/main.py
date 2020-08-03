# Prints the position of every occurrence of the substring t in s, with the first character of s having the position 1.

s = input("s")
t = input("t")
list_of_positions = []

x = 0

for x in range(0, len(s)):
	if s[x:x + len(t)] == t:
		list_of_positions.append(x+1)
	
print(list_of_positions)

