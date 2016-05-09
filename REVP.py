import sys

names = []
seqs = []

with open (sys.argv[1], "r") as fin:
	for string in fin:
		string = string.replace("\n", "")
		if string[0] == ">":
			names.append(string)
			seqs.append("")
		else:
			try:
				seqs[len(seqs)-1] += string
			except:
				seqs.append(string)

sequence = seqs[0].rstrip()
complement_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
dinuc = []

for i in range(len(sequence) - 1):
	if sequence[i] == complement_dict[sequence[i+1]]:
		dinuc.append(i)

palindromes = []
for d in dinuc:
	moving = d-1						## Move to the left untill we are within palindrome
	while True:
		if d + 2 + (d - moving) > len(sequence) or moving < 0:
			break
		if sequence[moving] == complement_dict[sequence[d + 1 + (d - moving)]]:
			moving -= 1
			if d - moving > 1 and d - moving < 7:
				palindromes.append([moving + 2, (d - moving) * 2])		## + 2 because of numeration from 1
		else:
			break									
			
for pal in palindromes:
	print pal[0], ' ', pal[1]
