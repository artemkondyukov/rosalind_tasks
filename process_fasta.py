def process_fasta(filename):
	output = dict()

	with open(filename, "r") as f:
		for line in f:
			if line[0] == ">":
				current_key = line[1:].strip()
				output[current_key] = ""
			else:
				output[current_key] += line.strip()

	return output
