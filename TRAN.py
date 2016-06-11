from utils import process_fasta

import sys

purines = ["A", "G"]
pyrimidines = ["T", "C", "U"]

first, second = process_fasta.as_array(sys.argv[1])

transitions = 0
transversions = 0
for f, s in zip(first.values()[0], second.values()[0]):
	if f == s:
		continue

	if (f in purines and s in purines) or (f in pyrimidines and s in pyrimidines):
		transitions += 1
	else:
		transversions += 1

print float(transitions) / float(transversions)
