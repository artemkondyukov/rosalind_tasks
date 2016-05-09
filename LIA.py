def one_all(g1, g2):
	return [g1*g2, g1*(1-g2) + g2*(1-g1), (1-g1)*(1-g2)]

factorial = lambda x: factorial(x - 1) * x if x > 1 else 1

def get_children(g1, g2):
	res = [0] * 9
	A = one_all(g1[0], g2[0])
	B = one_all(g1[1], g2[1])

	for i in range (0, 9):
		res[i] = A[i/3] * B[i%3]
	return res

string = raw_input()

data = [int(s) for s in string.split() if s.isdigit()]

orgs = []
neworgs = [0] * 9

for i in range (0, 3):
	for j in range (0, 3):
		orgs.append([0, i*0.5, j*0.5])

for i in range (0, len(orgs)):
	if orgs[i] == [0, 0.5, 0.5]:
		orgs[i][0] = 1

for i in range (0, data[0]):
	for j in range (0, 9):
		arr = get_children(orgs[8-j][1:3], [0.5, 0.5])
		for k in range (0, 9):
			neworgs[k] += arr[k] * orgs[j][0]
		print neworgs
	print "\n"
	for j in range (0, 9):
		orgs[j][0] = neworgs[j]
		neworgs[j] = 0

#print 1-((1-orgs[4][0]) ** (2 ** data[0]))
res = 0

for i in range (0, data[1]):
	res += factorial(2**data[0]) / factorial(i) / factorial(2**data[0]-i) * ((1-orgs[4][0])**(2**data[0] - i) * orgs[4][0] ** (i))
print 1-res
