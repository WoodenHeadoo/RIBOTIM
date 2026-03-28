from Mutants import *
from MRs import *

muid = 7

cases = []
fr = open('test_cases.txt','r')
row = fr.readline()
while row:
    row = row.strip()
    temp = row.split(' ')
    cas = []
    if '.' in row:
        for i in range(len(temp)):
            cas.append(float(temp[i]))
    else:
        for i in range(len(temp)):
            cas.append(int(temp[i]))
    cases.append(cas)
    row = fr.readline()
fr.close()

n = len(cases)
u1 = MRs()
u2 = Mutants()
fw = open('results_mutant'+str(muid)+'.txt','w')
fw.write(str(n))
err_cases = {}
for i in range(n):
    O = getattr(u2,'Origin')(cases[i],3)
    OO = getattr(u2,'Mutant'+str(muid))(cases[i],3)
    if abs(O - OO) > 1e-4:
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
    O1 = getattr(u2,'Mutant'+str(muid))(cases[int(temp[0])],3)
    O2 = getattr(u2,'Mutant'+str(muid))(cases[int(temp[1])],3)
    if getattr(u1,'MRO'+temp[2])(O1,O2):
        fw.write(temp[0]+' '+temp[1]+' 0\n')
        if int(temp[0]) in err_cases or int(temp[1]) in err_cases:
            count += 1
    else:
        fw.write(temp[0]+' '+temp[1]+' 1\n')
    row = fr.readline()
fr.close()
fw.close()
print('# false satisfaction: '+str(count))
