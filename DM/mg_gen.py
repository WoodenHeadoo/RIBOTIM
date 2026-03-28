import random
import math
from Mutants import *
from MRs import *

n = 5000
cases = [[2, 7, 8, 1, 2, 7, 8, 8, 1], [7, 4, 6, 8, 4, 0, 5, 0, 0],
        [0, 4, 6, 8, 0, 0, 5, 0, 0],[2, 0, 1, 3, 8, 2, 6, 4, 9],
        [2, 0, 0, 1, 5, 0, 2, 4, 6], [0, 0, 0, 1, 0, 0, 2, 4, 0]]
u1 = MRs()
u2 = Mutants()
fw1 = open('test_cases.txt','w')
for i in range(6):
    fw1.write(str(cases[i][0]))
    for j in range(1,9):
        fw1.write(' '+str(cases[i][j]))
    fw1.write('\n')
fw2 = open('metamorphic_groups.txt','w')
#fw2.write(str(n+6)+'\n')

group = []
for i in range(6):
    group.append([i])
count = 6
while count < n+6:
    gid = math.ceil((count-5)*6/n)-1
    cid = random.choice(group[gid])
    mrid = random.choice(range(1,11))
    ncase = getattr(u1,'MRI'+str(mrid))(cases[cid])
    if ncase is not None:
        fw1.write(str(ncase[0]))
        for j in range(1,9):
            fw1.write(' '+str(ncase[j]))
        fw1.write('\n')
        fw2.write(str(count)+' '+str(cid)+' '+str(mrid)+'\n')
        cases.append(ncase)
        group[gid].append(count)
        count += 1
        O1 = getattr(u2,'Origin')(cases[cid],3)
        O2 = getattr(u2,'Origin')(ncase,3)
        if not getattr(u1,'MRO'+str(mrid))(O1,O2):
            print(cases[cid])
            print(ncase)
            print(mrid)
fw1.close()
fw2.close()
"""
for i in range(6):
    res = getattr(utility,'Origin')(source_cases[i],3)
    print(res)
for i in range(6):
    for j in range(1,8):
        res = getattr(utility,'Mutant'+str(j))(source_cases[i],3)
        print(res)

for i in range(6):
    for j in range(1,11):
        O1 = getattr(utility,'Origin')(source_cases[i],3)
        follow = getattr(u2,'MRI'+str(j))(source_cases[i])
        if follow is not None:
            O2 = getattr(utility,'Origin')(follow,3)
            if not getattr(u2,'MRO'+str(j))(O1,O2):
                print(str(i)+' '+str(j))
                print(str(O1)+' '+str(O2))
"""
