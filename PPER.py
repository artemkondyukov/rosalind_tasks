import sys

n = int(sys.argv[1])
k = int(sys.argv[2])

# Yeah, I can use math.factorial, but it's boring :)
result = 1
for i in range(k):
	result *= n-i
	result %= 1000000

print result
