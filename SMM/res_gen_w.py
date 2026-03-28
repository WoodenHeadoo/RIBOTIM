from SMM import *
from MRs import *

muid = 1

cases = []
mar = [[],[]]
pos = 0
fr = open('test_cases.txt','r')
row = fr.readline()
while row:
    row = row.strip()
    temp = row.split(' ')
    for i in range(len(temp)):
        temp[i] = int(temp[i])
    if pos < 4:
        mar[0].append(temp)
        pos += 1
    else:
        mar[1].append(temp)
        pos += 1
        if pos == 8:
            cases.append(mar)
            mar = [[],[]]
            pos = 0
    row = fr.readline()
fr.close()

n = len(cases)
u1 = SMM()
u2 = SMMFactory(muid).getSMM()
u3 = MRs()
fw = open('w_results_mutant'+str(muid)+'.txt','w')
fw.write(str(n))
err_cases = {}
for i in range(n):
    O1 = u1.MatMul(cases[i][0],cases[i][1])
    O2 = u2.MatMul(cases[i][0],cases[i][1])
    if AssertMRViolation(O1,O2):
        fw.write(' '+str(i))
        err_cases[i] = None
fw.write('\n')
print('# wrong test cases: '+str(len(err_cases)))

count = 0
fr = open('metamorphic_groups.txt','r')
row = fr.readline()
while row:
    row = row.strip()
    temp = row.split(' ')
    OO = u2.MatMul(cases[int(temp[0])][0],cases[int(temp[0])][1])
    O = u2.MatMul(cases[int(temp[1])][0],cases[int(temp[1])][1])
    if getattr(u3,'MRO'+temp[2])(cases[int(temp[1])][0],cases[int(temp[1])][1],O,OO):
        if int(temp[0]) not in err_cases and int(temp[1]) not in err_cases:
            fw.write(temp[0]+' '+temp[1]+' 0\n')
        else:
            count += 1
    else:
        fw.write(temp[0]+' '+temp[1]+' 1\n')
    row = fr.readline()
fr.close()
fw.close()
print('# false satisfaction: '+str(count))
