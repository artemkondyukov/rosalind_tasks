def direct():
	with open("codon_table", "r") as f:
		output = dict()
		for line in f:
			raw = [l for l in line.strip().split(" ") if len(l) > 0]
			output.update({key: value for key, value in zip(raw[0::2], raw[1::2])})
	return output

def reverse():
	with open("codon_table", "r") as f:
		output = dict()
		for line in f:
			raw = [l for l in line.strip().split(" ") if len(l) > 0]
			for key, value in zip(raw[1::2], raw[0::2]):
				if key in output:
					output[key].append(value)
				else:
					output[key] = [value]
	return output

