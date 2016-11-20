#!/home/fonturacetamum/anaconda3/bin/python

complement = {}
complement["DNA"] = {"A": "T", "C": "G", "G": "C", "T": "A"}
complement["RNA"] = {"A": "Y", "C": "G", "G": "C", "U": "A"}

def reverse_complement(string, strand="DNA"):
	return "".join(map(lambda x: complement[strand][x], string[::-1]))
