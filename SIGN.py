import itertools
import sys

assert(len(sys.argv) == 2)
n = int(sys.argv[1])
lst = [item for sublist in map(lambda v: list(itertools.product(*v)), map(lambda x: [[v, -v] for v in x], itertools.permutations(range(1, n+1)))) for item in sublist]
print len(lst)
for i in lst:
	for v in i:
		print v,
	print
