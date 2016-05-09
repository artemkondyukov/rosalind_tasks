from sets import Set
import re

cod_aa = dict()
with open("codon_table", "r") as fin: 
    for string in fin:
        pat = re.compile(r'([ACGU]*)([\s]*)([A-Za-z]+)([\s]*)([ACGU]*)([\s]*)([A-Za-z]+)([\s]*)([ACGU]*)([\s]*)([A-Za-z]+)([\s]*)([ACGU]*)([\s]*)([A-Za-z]+)')
        sea = pat.search(string)
        for i in range(0,4):
            codon = sea.group(i*4+1)
            aa = sea.group(i*4+3)
            cod_aa[codon.replace("U", "T")] = aa			# Further we use DNA seq instead of RNA, so we need to replace uracyl with thymidine

def my_range(start, end, step):
    while start < end:
        yield start
        start += step

names = []
seqs = []

with open ("orf.in", "r") as fin:
	for str in fin:	
		str = str.replace("\n", "")
		if str[0] == ">":
			names.append(str)
			seqs.append("")
			continue
		seqs[len(seqs)-1] += str

for seq in seqs:
	results = Set()
	revcomp = seq.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")		#lower case is used for distinguish between 'new' and 'old' N
	revcomp = revcomp.replace("a", "A").replace("c", "C").replace("g", "G").replace("t", "T")
	revcomp = revcomp[len(revcomp)-1::-1]
	pat = re.compile(r'ATG((([ACGT]){3})*?)(TAG|TAA|TGA)')
	searchFrom = 0
	result = pat.search(seq)
	while result is not None:
		substr = seq[result.start():result.end()]
		if substr not in results:
			results.add(substr)
		searchFrom = result.start()+1
		result = pat.search(seq, searchFrom)

	searchFrom = 0								# We use two loops for convenience
	result = pat.search(revcomp)
	while result is not None:
		substr = revcomp[result.start():result.end()]
		if substr not in results:
			results.add(substr)
		searchFrom = result.start()+1
		result = pat.search(revcomp, searchFrom)

	prot_res = Set()
	for res in results:
		prot_seq = ""
		for i in my_range(0, len(res), 3):
			next_aa = cod_aa[res[i:i+3]]
			if next_aa != "Stop":
				prot_seq += next_aa
		prot_res.add(prot_seq)

	for prot in prot_res:
		print prot
