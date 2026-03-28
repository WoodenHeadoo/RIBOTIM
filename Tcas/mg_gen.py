import random
import math
from TCAS import *
from MRs import *

n = 5000
k = 200
cases = []
fw1 = open('test_cases.txt','w')
for i in range(k):
    argv = [0 for _ in range(12)]
    if i < 10:
        argv[0] = 500
        argv[1] = 1
        argv[2] = 1
        argv[4] = 600
        argv[9] = 0
        argv[10] = 0
    elif i < 20:
        argv[0] = 700
        argv[1] = 1
        argv[2] = 1
        argv[4] = 600
        argv[9] = 1
        argv[10] = 1
    else:
        argv[0] = 700
        argv[1] = 1
        argv[2] = 1
        argv[4] = 600
        argv[9] = 0
        argv[10] = 1
    if random.random() > 0.5:
        argv[3] = 30
        argv[5] = 70
    else:
        argv[3] = 70
        argv[5] = 30
    argv[6] = random.choice([0,1,2,3])
    temp = random.sample(list(range(301,801)),2)
    argv[7] = temp[0]
    argv[8] = temp[1]
    argv[11] = random.choice([0,1])
    cases.append(argv)
    fw1.write(str(argv[0]))
    for j in range(1,12):
        fw1.write(' '+str(argv[j]))
    fw1.write('\n')

u1 = MRs()
u2 = TCAS()
group = []
for i in range(k):
    group.append([i])
count = k
fw2 = open('metamorphic_groups.txt','w')
while count < n+k:
    gid = math.ceil((count-k+1)*k/n)-1
    cid = random.choice(group[gid])
    mrid = random.choice(range(1,10))
    ftc = getattr(u1,'MR'+str(mrid))(cases[cid])
    fw1.write(str(ftc[0]))
    for j in range(1,12):
        fw1.write(' '+str(ftc[j]))
    fw1.write('\n')
    fw2.write(str(count)+' '+str(cid)+' '+str(mrid)+'\n')
    cases.append(ftc)
    group[gid].append(count)
    count += 1
    O = u2.Tcas(cases[cid])
    OO = u2.Tcas(ftc)
    if not O == OO:
        print(cases[cid])
        print(cases[-1])
        print(mrid)
        print(O)
        print(OO)
fw1.close()
fw2.close()
"""
for i in range(len(cases)):
    for j in range(1,9):
        ftc = getattr(u1,'MR'+str(j))(cases[i])
        O = u2.Tcas(cases[i])
        OO = u2.Tcas(ftc)
        if not O == OO:
            print(cases[i])
            print(ftc)
            print(j)

s = 'Mutant'+str(11)
u3 = TCASFactory(s).getTCAS()
count = 0
for i in range(len(cases)):
    for j in range(1,9):
        ftc = getattr(u1,'MR'+str(j))(cases[i])
        O = u3.Tcas(cases[i])
        OO = u3.Tcas(ftc)
        if not O == OO:
            count += 1
print(count)
"""
