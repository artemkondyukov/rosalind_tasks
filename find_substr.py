str = raw_input()
substr = raw_input()

cursor = 0
pos = []
matches = []
result = []
for i in range(0, len(str)):
    if str[i] == substr[0]:
        matches.append(i)
    if len(matches) > 50 or i == len(str)-1:
#        print len(matches)
        while len(matches) > 0:
            j = 0
            while str[matches[0]+j] == substr[j]:
                if j == len(substr)-1:
                    result.append(matches[0])
                    break
                if j+matches[0] == len(str)-1:
                    break
                j += 1
            del matches[0]

for i in range(0, len(result)):
    print result[i]+1,
print
