from TCAS import *
from MRs import *

cases = []
fr = open('test_cases.txt','r')
row = fr.readline()
while row:
    row = row.strip()
    temp = row.split(' ')
    cas = []
    for i in range(len(temp)):
        if '.' in temp[i]:
            cas.append(int(float(temp[i])))
        else:
            cas.append(int(temp[i]))
    cases.append(cas)
    row = fr.readline()
fr.close()

n = len(cases)
u2 = TCAS()
for muid in range(7,8):
    u3 = TCASFactory('Mutant'+str(muid)).getTCAS()
    fw = open('results_mutant'+str(muid)+'.txt','w')
    fw.write(str(n))
    err_cases = {}
    for i in range(n):
        O = u2.Tcas(cases[i])
        OO = u3.Tcas(cases[i])
        if not O == OO:
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
        O1 = u3.Tcas(cases[int(temp[0])])
        O2 = u3.Tcas(cases[int(temp[1])])
        if O1 == O2:
            fw.write(temp[0]+' '+temp[1]+' 0\n')
            if int(temp[0]) in err_cases and int(temp[1]) in err_cases:
                count += 1
        else:
            fw.write(temp[0]+' '+temp[1]+' 1\n')
        row = fr.readline()
    fr.close()
    fw.close()
    print('# false satisfaction: '+str(count))
