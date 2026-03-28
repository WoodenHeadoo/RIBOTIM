import random
import math
from KNN import *
from MRs import *
from decimal import Decimal

n = 5000
rawdata = []
fr = open('iris.data','r')
row = fr.readline()
while row:
    row = row.strip()
    temp = row.split(',')
    for i in range(len(temp)-1):
        temp[i] = Decimal(temp[i])
    rawdata.append(temp)
    row = fr.readline()
fr.close()

cases = []
fw1 = open('test_cases.txt','w')
order = list(range(150))
for k in range(200):
    random.shuffle(order)
    training_set = []
    testing_set = []
    for i in range(90):
        temp = []
        s = ''
        for j in range(5):
            temp.append(rawdata[order[i]][j])
            s += str(rawdata[order[i]][j]) + ','
        training_set.append(temp)
        fw1.write(s.rstrip(',')+'\n')
    temp = []
    s = ''
    for j in range(5):
        temp.append(rawdata[order[90]][j])
        s += str(rawdata[order[90]][j]) + ','
    testing_set.append(temp)
    fw1.write(s.rstrip(',')+'\n')
    cases.append([training_set,testing_set])

u1 = MRs()
u2 = KNN()
group = []
for i in range(200):
    group.append([i])
count = 200
fw2 = open('metamorphic_groups.txt','w')
while count < n+200:
    gid = math.ceil((count-199)*200/n)-1
    cid = random.choice(group[gid])
    mrid = random.choice(range(1,5))
    ftc_train,ftc_test = getattr(u1,'MR'+str(mrid))(cases[cid][0],cases[cid][1])
    for i in range(90):
        s = ''
        for j in range(5):
            s += str(ftc_train[i][j]) + ','
        fw1.write(s.rstrip(',')+'\n')
    s = ''
    for j in range(5):
        s += str(ftc_test[0][j]) + ','
    fw1.write(s.rstrip(',')+'\n')
    fw2.write(str(count)+' '+str(cid)+' '+str(mrid)+'\n')
    cases.append([ftc_train,ftc_test])
    group[gid].append(count)
    count += 1
    u2.setInput(cases[cid][0],cases[cid][1])
    O1 = u2.getPredications()
    u2.setInput(ftc_train,ftc_test)
    O2 = u2.getPredications()
    if not (O1[0] == O2[0]):
        print(cases[cid])
        print(ncase)
        print(mrid)
fw1.close()
fw2.close()
