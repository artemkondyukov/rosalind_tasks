#!/home/fonturacetamum/anaconda3/bin/python

from utils.process_fasta import *

results = {}
def count_matchings(string, start, end, counters):
	if (start, end) in results:
		return results[(start, end)]

	# if the string is empty, it has onlt one way to be matched (trivial),
	# whereas if string is not empty we set result to 0 and consider different possible matchings
	result = 1 if len(string) == 0 else 0

	# Go through the string so as to find possible complements of the first letter
	# 'Possible' means that betweene the first element and the element chosen there must 
	# be a way to complement every letter. 
	# I.e.: AGUACU. Here we can't match the first 'A' with the the third 'U',
	# Whereas it's possible to complement the first 'A' with the last 'U'.
	for i, ch in enumerate(string[1:]):
		if string[0] == complement[ch]:
			if (counters[i+1]["A"] - (string[0] == "A")) == (counters[i+1]["U"] - (string[0] == "U")) and \
			   (counters[i+1]["C"] - (string[0] == "C")) == (counters[i+1]["G"] - (string[0] == "G")):
				current_result = 1
				left_counters = [dict((k, v - counters[1][k]) for k, v in counter.items()) for counter in counters[1:i+1]]
				right_counters = [dict((k, v - counters[i+2][k]) for k, v in counter.items()) for counter in counters[i+2:]]
				current_result *= count_matchings(string[1:i+1], start+1, start+i+1, left_counters)
				current_result *= count_matchings(string[i+2:], start+i+2, end, right_counters)
				result += current_result

	# We shouldn't compute the result value for a start-end pair more than once.
	results[(start, end)] = result
	return result % 1000000

complement = {"A": "U", "C": "G", "G": "C", "U": "A"}
seq = process_fasta("CAT.in")

# counters array represents how many different letters took place before current.
counters = []
counters.append({"A": 0, "C": 0, "G": 0, "U": 0})
for ch in seq[:-1]:
	counters.append(dict(counters[-1]))
	counters[-1][ch] += 1

# here we interested in the first (and only) sequence within the file
for v in seq.values():
	seq = v
	break

print(count_matchings(seq, 0, len(seq), counters))
