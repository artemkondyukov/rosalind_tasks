import re

string = raw_input()
pat = re.compile(r'([0-9]*)([\s]*)([0-9]*)')
n = int(pat.search(string).group(1))
m = int(pat.search(string).group(3))

rabs = [0 for x in range(m)]
rabs[0] = 1

for date in range(2, n+1):
    new_r = [0 for x in range(m)]
    for age in range(1, m):
        new_r[0] += rabs[age]
    for age in range(0, m-1):
        new_r[age+1] = rabs[age]
    for age in range(0, m):
        rabs[age] = new_r[age]
print sum(rabs)
