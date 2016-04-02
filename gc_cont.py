max_gc = 0.0
max_gc_info = ""
nextinfo = ""
while True:
    if nextinfo != None and nextinfo != "" and nextinfo[0] == ">":
        if nextinfo == ">":
            break
        info = nextinfo
    else:
        info = raw_input()
    strain = ""
    getting_sequence = True
    while getting_sequence:
        strn = raw_input()
        if strn[0] == ">":
            nextinfo = strn
            getting_sequence = False
        else:
            strain += strn
    gc = 0.0
    for i in range (0, len(strain)):
        if strain[i] == "C" or strain[i] == "G":
            gc += 1
    gc /= len(strain)
    if gc > max_gc:
        max_gc = gc
        max_gc_info = info[1:]

print max_gc_info + "\n" + str(max_gc)
