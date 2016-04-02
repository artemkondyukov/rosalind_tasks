diff = 0
str1 = raw_input()
str2 = raw_input()
for i in range(0, len(str1)):
    if str1[i] != str2[i]:
        diff += 1

print diff
