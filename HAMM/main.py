A = input("string 1")
B = input("string 2")
x = 0
diff = 0

for x in range(0, len(A)):
	if A[x] != B[x]:
		diff = diff + 1
		
print(diff)
