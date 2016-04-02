import re

cod_aa = dict()
with open("codon_table", "r") as fin: 
	for string in fin:
		pat = re.compile(r'([ACGU]*)([\s]*)([A-Za-z]+)([\s]*)([ACGU]*)([\s]*)([A-Za-z]+)([\s]*)([ACGU]*)([\s]*)([A-Za-z]+)([\s]*)([ACGU]*)([\s]*)([A-Za-z]+)')
		sea = pat.search(string)
		for i in range(0,4):
#        		codon = sea.group(i*4+1)
			aa = sea.group(i*4+3)
			if aa in cod_aa:
				cod_aa[aa] += 1
			else:
				cod_aa[aa] = 1

with open("inferr_mrna.in", "r") as fin:
	variants = 1
	for string in fin:
		string = string.replace("\n", "")
		for x in range (len(string)):
			variants *= cod_aa[string[x]]
			variants %= 1000000
	variants *= 3						#STOP codon
	variants %= 1000000

print variants
