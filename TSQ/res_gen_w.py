from TSQ import *
from MRs import *

muid = 6

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
u2 = Trisquare()
u3 = TriFactory('Mutant'+str(muid)).getTri()
fw = open('w_results_mutant'+str(muid)+'.txt','w')
fw.write(str(n))
err_cases = {}
for i in range(n):
    O = u2.trisquare(cases[i])
    OO = u3.trisquare(cases[i])
    if not u1.MRO(O,OO):
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
    O1 = u3.trisquare(cases[int(temp[0])])
    O2 = u3.trisquare(cases[int(temp[1])])
    if u1.MRO(O1,O2):
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
