### Importing the FASTA file sequences into a list
from Bio import SeqIO
seqs = [str(rec.seq) for rec in SeqIO.parse("raw.fasta", "fasta")]

seqs.sort(key=len)
reference = seqs[0]
del seqs[0]
# Now we have a reference : the shortest sequence, and a list of the other sequences

results = ""
longest_common_sequence = ""

def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        for j in range(len2):
            lcs_temp=0
            match=''
            while ((i+lcs_temp < len1) and (j+lcs_temp<len2) and string1[i+lcs_temp] == string2[j+lcs_temp]):
                match += string2[j+lcs_temp]
                lcs_temp+=1
            if (len(match) > len(answer)):
                answer = match
    return answer
# Function that finds the longest common substring between two strings


for i in range(len(seqs)):
	answer = longestSubstringFinder(reference, seqs[i])
	if len(answer) > len(results):
		x = 0
		for i in range(len(seqs)):
			if answer in seqs[i]:
				x = x + 1
		if x == len(seqs):
			results = answer

print(results)
