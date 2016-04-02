import sys
from process_fasta import *

#Obtain first name of sequence -- mRNA sequence
with open(sys.argv[1], "r") as f:
	for line in f:
		mrna_key = line[1:].strip()
		break

seqs = process_fasta(sys.argv[1])
print seqs[mrna_key]
