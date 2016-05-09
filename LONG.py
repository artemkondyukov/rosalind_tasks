import sys

from utils import process_fasta

"""
Shortest superstring problem
Here I implement the greedy approach
"""

def compute_overlap(str1, str2):
	# str2 is a suffix of str1
	l1 = len(str1)
	l2 = len(str2)
	result = 0
	if l1 < l2:
		for i in range(l1):
			if str1[i:] == str2[0:l1-i]:
				result = l1 - i
				break

	else:
		for i in range(l2):
			if str1[l1-l2+i:] == str2[0:l2-i]:
				result = l2 - i
				break
	return result
		

seqs = process_fasta.process_fasta(sys.argv[1])

overlap_matrix = []
# strings from rows have strings from columns as suffixes, therefore the matrix isn't symmetric
for s_r in seqs.values():
	overlap_matrix.append([])
	for s_c in seqs.values():
		if s_r == s_c:
			overlap_matrix[-1].append(-1)
		else:
			overlap_matrix[-1].append(compute_overlap(s_r, s_c))

constr_dict = dict()
has_pred = [False] * len(overlap_matrix)
taken = []
for i, r in enumerate(overlap_matrix):
	if max(r) * 2 < len(seqs.values()[i]):
		constr_dict[i] = (-1, 0)
		continue

	if r.index(max(r)) not in taken:
		taken.append(r.index(max(r)))
	else:
		while True:
			if r[r.index(max(r))] == -1:
				taken.append(-1)
				break

			r[r.index(max(r))] = -1
			if r.index(max(r)) not in taken:
				taken.append(r.index(max(r)))
				break
	if taken[-1] != -1:
		has_pred[taken[-1]] = True
	constr_dict[i] = (taken[-1], max(r))

index = has_pred.index(False)
prev_len = 0
final_string = ""
while index != -1:
	if has_pred[index] == False:
		final_string += seqs.values()[index]
	else:
		final_string += seqs.values()[index][prev_len:]

	prev_len = constr_dict[index][1]
	index = constr_dict[index][0]

print final_string
