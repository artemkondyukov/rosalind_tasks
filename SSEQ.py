from utils import process_fasta

import sys

assert(len(sys.argv) > 1)
string, substring = process_fasta.as_array(sys.argv[1])
string = string.values()[0]
substring = substring.values()[0]

pos = 0
for sub_ch in substring:
	for str_ch in string[pos:]:
		if sub_ch == str_ch:
			print pos + 1,
			pos += 1
			break
		pos += 1

