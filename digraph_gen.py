import random

for i in range(10000):
    print ">Rosalind_" + str(i)
    max = random.randint(100, 1000)
    res = ""
    for i in range(0, max):
        res += random.choice('ACGT')
    print res
