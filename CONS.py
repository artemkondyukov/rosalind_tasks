def add_curr_seq(curr_seq, matr):
    for i in range (0, len(current_seq)):
        matr[current_seq[i]][i] += 1
    return

length  = 0
current_seq = ""
matr = dict()
cons = ""
with open("consensus_in", "r") as fin:
    for string in fin:
        if string[0] == ">":
            if len(current_seq) != 0:
                if len(matr) == 0:
                    matr['A'] = [0 for x in range(len(current_seq))]
                    matr['C'] = [0 for x in range(len(current_seq))]
                    matr['G'] = [0 for x in range(len(current_seq))]
                    matr['T'] = [0 for x in range(len(current_seq))]
                add_curr_seq(current_seq, matr)
            current_seq = ""
        else:
            current_seq += string.rstrip()
add_curr_seq(current_seq, matr)


for i in range(0, len(matr['A'])):
    con_int = max(matr['A'][i], matr['C'][i], matr['G'][i], matr['T'][i])
    conchar = "!"
    for key in ('A', 'C', 'G', 'T'):
        if matr[key][i] == con_int:
            conchar = key
            break
    cons += conchar

print cons
for n in ('A', 'C', 'G', 'T'):
    for i in range(0, len(matr[n])):
        if i == 0:
            print "%c: %d" % (n, matr[n][i]),
            continue
        print matr[n][i],
    print
