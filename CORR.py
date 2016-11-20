#!/home/fonturacetamum/anaconda3/bin/python

from utils.process_fasta import process_fasta
from utils.reverse_complement import reverse_complement

seq = process_fasta("CORR.in")

# Let reverse-complement every string which doesn't start with A or T
print(seq)
for k, v in seq.items():
	if v[0] not in ['A', 'C']:
		seq[k] = reverse_complement(v)
print(seq)

sorted_strands = sorted(seq.values())
sorted_set = set()
set_add = sorted_set.add
duplicates = [strand for strand in sorted_strands if (strand in sorted_set or sorted_set.add(strand))]
sorted_strands = [strand for strand in sorted_strands if strand not in duplicates]

print(sorted_strands)
print(duplicates)
