import re

arr = dict()

pat = re.compile(r'([A-Z]*)([\s]*)([0-9.]*)')

with open("aa_weight_table") as fin:
	for line in fin:
		m = re.search(pat, line)
		arr[m.group(1)] = float(m.group(3))

result = 0
with open("calc_prot_mass.in") as fin:
	for line in fin:
		line = line.rstrip()
		for i in range(len(line)):
			result += arr[line[i]]

print result
