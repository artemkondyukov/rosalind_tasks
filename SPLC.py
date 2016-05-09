import sys

from utils import get_codon_table, process_fasta

#Obtain first name of sequence -- mRNA sequence
with open(sys.argv[1], "r") as f:
	for line in f:
		mrna_key = line[1:].strip()
		break

seqs = process_fasta.process_fasta(sys.argv[1])
mrna = seqs[mrna_key]
del seqs[mrna_key]

for key in seqs:
	mrna = mrna.replace(seqs[key], "")

codon_table = get_codon_table.direct("utils/codon_table")
mrna_codons = [mrna[3*l:3*l+3] for l in range(len(mrna) / 3)]

acids = ""
for codon in mrna_codons:
	if codon_table[codon.replace("T", "U")] != 'Stop':
		acids += codon_table[codon.replace("T", "U")]

print acids
