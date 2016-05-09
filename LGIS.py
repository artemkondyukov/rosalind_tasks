def longest_increasing_subsequence(sequence):
	counts = [1]  * len(sequence)
	path = [-1] * len(sequence)
	for i in range(1, len(sequence)):
		for j in range(0, i):
			if sequence[i] > sequence[j] and counts[j] >= counts[i]:
 				counts[i] = counts[j] + 1
				path[i] = j

	index = counts.index(max(counts))
	result = []
	while index != -1:
		result.insert(0, sequence[index])
		index = path[index]
	return result

def longest_decreasing_subsequence(sequence):
	counts = [1]  * len(sequence)
	path = [-1] * len(sequence)
	for i in range(1, len(sequence)):
		for j in range(0, i):
			if sequence[i] < sequence[j] and counts[j] >= counts[i]:
				counts[i] = counts[j] + 1
				path[i] = j

	index = counts.index(max(counts))
	result = []
	while index != -1:
		result.insert(0, sequence[index])
		index = path[index]
	return result

with open("longest_increasing_subsequence.in", "r") as f:
	length = int(f.readline())
	raw_str = f.readline().strip().split(" ")
	sequence = [int(i) for i in raw_str]

	increasing = longest_increasing_subsequence(sequence)
	decreasing = longest_decreasing_subsequence(sequence)
	
	for i in increasing:
		print i,
	print

	for i in decreasing:
		print i,
	print
