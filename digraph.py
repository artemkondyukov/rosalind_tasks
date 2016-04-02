import time
t = time.time()
def qsort(l):
    if l == []:
        return []
    pivot = l[0]
    lesser = qsort([x for x in l[1:] if x[1] < pivot[1]])
    greater = qsort([x for x in l[1:] if x[1] >= pivot[1]])
    return lesser + [pivot] + greater

suffs = []
prefs = []
current_seq = ""
with open("digraph_in", "r") as fin:
    for string in fin:
        if string[0] == ">":
            if len(current_seq) != 0:
                suffs.append([curr_name.rstrip(), current_seq[-3:]])
                prefs.append([curr_name.rstrip(), current_seq[:3]])
            current_seq = ""
            curr_name = string[1:]
        else:
            current_seq += string.rstrip()
if len(current_seq) != 0:
    suffs.append([curr_name.rstrip(), current_seq[-3:]])
    prefs.append([curr_name.rstrip(), current_seq[:3]])

suffs = qsort(suffs)
prefs = qsort(prefs)

i = 0
prevsuf = ""
while len(suffs) > i:
    j = 0
#    print "suf: ", suffs[i]
    while len(prefs) > j:
#        print "pref: ", prefs[j]
        if prefs[j][1] == suffs[i][1]:
            if prefs[j][0] != suffs[i][0]:
                print suffs[i][0] + " " + prefs[j][0]
#            else:
#                j += 1
#                continue
#        else:
#            if len(suffs) > 1 and suffs[1][1] != suffs[0][1] and j > 0:
#                del prefs[:j]
#                j = -1
#            if suffs[i][1] < prefs[j][1]:
#                break

        j += 1
#    del suffs[0]
    i += 1

print time.time() - t
