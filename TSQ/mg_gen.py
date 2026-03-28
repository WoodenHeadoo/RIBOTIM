import random
import math
from TSQ import *
from MRs import *

n = 5000
cases = []
fw1 = open('test_cases.txt','w')
while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    if a >= b + c or b >= a + c or c >= a + b:
        continue
    else:
        triangle = [a, b, c]
        fw1.write(str(a)+' '+str(b)+' '+str(c)+'\n')
        cases.append(triangle)
        if len(cases) >= 100:
            break

u1 = MRs()
u2 = Trisquare()
group = []
for i in range(100):
    group.append([i])
count = 100
fw2 = open('metamorphic_groups.txt','w')
while count < n+100:
    gid = math.ceil((count-99)*100/n)-1
    cid = random.choice(group[gid])
    mrid = random.choice(range(1,10))
    ftc = getattr(u1,'MRI'+str(mrid))(cases[cid])
    fw1.write(str(ftc[0])+' '+str(ftc[1])+' '+str(ftc[2])+'\n')
    fw2.write(str(count)+' '+str(cid)+' '+str(mrid)+'\n')
    cases.append(ftc)
    group[gid].append(count)
    count += 1
    O = u2.trisquare(cases[cid])
    OO = u2.trisquare(ftc)
    if not u1.MRO(O,OO):
        print(cases[cid])
        print(cases[-1])
        print(mrid)
        print(O)
        print(OO)
fw1.close()
fw2.close()
"""
for i in range(len(cases)):
    for j in range(1,10):
        ftc = getattr(u1,'MRI'+str(j))(cases[i])
        O = u2.trisquare(cases[i])
        OO = u2.trisquare(ftc)
        if not u1.MRO(O,OO):
            print(cases[i])
            print(ftc)
            print(j)

s = 'Mutant'+str(5)
u3 = TriFactory(s).getTri()
count = 0
for i in range(len(cases)):
    for j in range(1,10):
        ftc = getattr(u1,'MRI'+str(j))(cases[i])
        O = u3.trisquare(cases[i])
        OO = u3.trisquare(ftc)
        if not u1.MRO(O,OO):
            count += 1
print(count)
"""
