import random
import math
from SMM import *
from MRs import *

n = 5000
cases = []
fw1 = open('test_cases.txt','w')
for _ in range(50):
    mar = []
    for _ in range(2):
        temp = [[0] * 4 for k in range(4)]
        for i in range(4):
            s = ''
            for j in range(4):
                if random.random() < 0.4:
                    temp[i][j] = int(random.random()*10)
                s += str(temp[i][j]) + ' '
            fw1.write(s.rstrip(' ')+'\n')
        mar.append(temp)
    cases.append(mar)
for _ in range(10):
    mar = []
    temp = [[0] * 4 for k in range(4)]
    for i in range(4):
        s = ''
        for j in range(4):
            s += str(temp[i][j]) + ' '
        fw1.write(s.rstrip(' ')+'\n')
    mar.append(temp)
    temp = [[0] * 4 for k in range(4)]
    for i in range(4):
        s = ''
        for j in range(4):
            if random.random() < 0.4:
                temp[i][j] = int(random.random()*10)
            s += str(temp[i][j]) + ' '
        fw1.write(s.rstrip(' ')+'\n')
    mar.append(temp)
    cases.append(mar)
for _ in range(10):
    mar = []
    temp = [[0] * 4 for k in range(4)]
    for i in range(4):
        s = ''
        for j in range(4):
            if random.random() < 0.4:
                temp[i][j] = int(random.random()*10)
            s += str(temp[i][j]) + ' '
        fw1.write(s.rstrip(' ')+'\n')
    mar.append(temp)
    temp = [[0] * 4 for k in range(4)]
    for i in range(4):
        s = ''
        for j in range(4):
            s += str(temp[i][j]) + ' '
        fw1.write(s.rstrip(' ')+'\n')
    mar.append(temp)
    cases.append(mar)

u1 = MRs()
u2 = SMM()
group = []
for i in range(70):
    group.append([i])
count = 70
fw2 = open('metamorphic_groups.txt','w')
while count < n+70:
    gid = math.ceil((count-69)*70/n)-1
    cid = random.choice(group[gid])
    mrid = random.choice(range(1,16))
    ftc_A, ftc_B = getattr(u1,'MRI'+str(mrid))(cases[cid][0],cases[cid][1])
    for i in range(4):
        s = ''
        for j in range(4):
            s += str(ftc_A[i][j]) + ' '
        fw1.write(s.rstrip(' ')+'\n')
    for i in range(4):
        s = ''
        for j in range(4):
            s += str(ftc_B[i][j]) + ' '
        fw1.write(s.rstrip(' ')+'\n')
    fw2.write(str(count)+' '+str(cid)+' '+str(mrid)+'\n')
    cases.append([ftc_A, ftc_B])
    group[gid].append(count)
    count += 1
    O = u2.MatMul(cases[cid][0],cases[cid][1])
    OO = u2.MatMul(ftc_A, ftc_B)
    if not getattr(u1,'MRO'+str(mrid))(cases[cid][0],cases[cid][1],O,OO):
        print(cases[cid])
        print(cases[-1])
        print(mrid)
fw1.close()
fw2.close()
"""
m = 4
n = 4
rho = 0.5
u1 = MRs()
#u2 = SMM()
u2 = SMMFactory(0).getSMM()
count = 0
for _ in range(10):
    mar = []
    for _ in range(2):
        temp = [[0] * n for k in range(m)]
        for i in range(m):
            for j in range(n):
                if random.random() < rho:
                    temp[i][j] = random.random()*10
        mar.append(temp)
    for k in range(1,16):
        O = u2.MatMul(mar[0],mar[1])
        ftc_A, ftc_B = getattr(u1,'MRI'+str(k))(mar[0],mar[1])
        OO = u2.MatMul(ftc_A, ftc_B)
        if not getattr(u1,'MRO'+str(k))(mar[0],mar[1],O,OO):
            count += 1
print(count)
"""
