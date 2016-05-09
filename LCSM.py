names = []
seqs = []
with open ("comm_substr.in", "r") as fin:
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

assert (len(names) == len(seqs))

len_of_substr = len(seqs[0])
got_it = False
result = False

i = 0

while i < len(seqs[0]) - (len_of_substr-1) and not result:
	tmp = seqs[0][i:i + (len_of_substr)]
	for j in xrange(1, len(seqs)):
		if tmp not in seqs[j]:
			break
		if j == len(seqs) - 1:
			result = True
	if i == len(seqs[0]) - (len_of_substr-1) - 1:
		if result:
			break
		len_of_substr -= 1
		i = 0
		continue
	i += 1

i -= 1
print seqs[0][i:i+len_of_substr]
