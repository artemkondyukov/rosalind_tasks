import math
import sys

from utils import process_fasta

seqs = process_fasta.process_fasta(sys.argv[1])
As = 0
for l in seqs.values()[0]:
	if l == 'A':
		As += 1

print math.factorial(As) * math.factorial(len(seqs.values()[0])/2 - As)
