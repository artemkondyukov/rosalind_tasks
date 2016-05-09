def perm(n):
	if not isinstance(n, list): return [n]
	if len(n) == 1: return n
	result = []
	for i in range(len(n)):
		recursive_res = perm(n[:i] + n[(i+1):])
		for j in range(len(recursive_res)):
			tmpArr = []
			tmpArr.append(n[i])
			if not isinstance (recursive_res[j], list):
				tmpArr.append(recursive_res[j])
			else:
				tmpArr.extend(recursive_res[j])
			result.append(tmpArr)
	return result

def factorial(n):
	if n < 1:
		return 1
	return n * factorial(n-1)

N = int(raw_input())

print factorial (N)
toOut = perm(range(1, N+1))

for perm in toOut:
	for num in perm:
		print num,
	print
