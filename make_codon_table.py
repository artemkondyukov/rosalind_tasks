import re

cod_aa = dict()
with open("codon_table", "r") as fin: 
    for string in fin:
        pat = re.compile(r'([ACGU]*)([\s]*)([A-Za-z]+)([\s]*)([ACGU]*)([\s]*)([A-Za-z]+)([\s]*)([ACGU]*)([\s]*)([A-Za-z]+)([\s]*)([ACGU]*)([\s]*)([A-Za-z]+)')
        sea = pat.search(string)
        for i in range(0,4):
            codon = sea.group(i*4+1)
            aa = sea.group(i*4+3)
            cod_aa[codon] = aa

#for key, value in cod_aa.iteritems():
#    print key + " " + value

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

prot = ""
with open("prot_in", "r") as fin:
    for string in fin:
        for i in my_range(0, len(string), 3):
            if i < len(string)-3:
                if cod_aa[string[i:i+3]] == "Stop":
                    break;
                prot += cod_aa[string[i:i+3]]

print prot
