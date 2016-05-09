import sys

from utils import process_fasta

def deBrujinConstruct():
	return []

seqs = process_fasta.process_fasta(sys.argv[1])

if len(sys.argv) > 2:
	k = int(sys.argv[2])
else:
	k = 4
