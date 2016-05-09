import re

str = raw_input()
nums = [int(s) for s in str.split() if s.isdigit()]

print nums

res = 0
res += nums[0] * 2
res += nums[1] * 2
res += nums[2] * 2
res += nums[3] * 1.5
res += nums[4]

print res
