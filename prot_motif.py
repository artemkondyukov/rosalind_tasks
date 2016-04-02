import urllib
import re

names = []
seqs = []

with open ("prot_motif.in", "r") as fin:
	for str in fin:	
		str = str.replace("\n", "")
		f = urllib.urlopen("http://www.uniprot.org/uniprot/" + str + ".fasta")
		for string in f:
			string = string.replace("\n", "")
			if string[0] == ">":
				names.append(str)
				seqs.append("")
				continue
			seqs[len(seqs)-1] += string

counter = 0
for d in seqs:
	pat = re.compile(r'(.*?)N[A-OQ-Z][ST][A-OQ-Z]')
	namePrinted = False
	startPos = 0
	s = pat.search(d, startPos)
	while s is not None:
		if not namePrinted:
			print names[counter]
			namePrinted = True
		print s.end() - 3,
		startPos = s.end() - 3
		s = pat.search(d, startPos)
	if namePrinted:					#If namePrinted is false there are no matches and we shouldn't print newline
		print ""
	counter += 1
