import re

#string = raw_input()
pat = re.compile(r'^([0-9]+) ([0-9]+) ([0-9]+)')
#k = float(pat.search(string).group()[0])
#l = float(pat.search(string).group()[2])
#m = float(pat.search(string).group()[4])
k = float(raw_input())
l = float(raw_input())
m = float(raw_input())
prob = 0.0
summ = k + l + m
prob += k / summ
prob += l * (l-1) / summ / (summ-1) * 3 / 4
prob += l * k / summ / (summ-1)
prob += m * l / summ / (summ-1)
prob += m * k / summ / (summ-1)
print prob
