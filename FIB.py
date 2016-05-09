n = int(input())
k = int(input())

rabs = []
summ = 0
rabs.append(1)
rabs.append(1)
for i in range(2, n):
    rabs.append(rabs[i-2]*k+rabs[i-1])
if n <= 2:
    print "1";
print rabs[len(rabs)-1]
