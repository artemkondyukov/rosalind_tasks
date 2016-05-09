import math
import sys

with open(sys.argv[1], "r") as f:
	string = f.readline().strip()
	gcs = [float(a) for a in f.readline().strip().split()]

for gc in gcs:
	pgc = math.log10(gc / 2)
	pat = math.log10(.5 - gc / 2)
	result = 0
	for l in string:
		result += pgc if l in ['G', 'C'] else pat
	print "%0.3f" % result,
