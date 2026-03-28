from KNN import *
from MRs import *
from decimal import Decimal

muid = 2

cases = []
training_set = []
testing_set = []
pos = 0
fr = open('test_cases.txt','r')
row = fr.readline()
while row:
    row = row.strip()
    temp = row.split(',')
    for i in range(len(temp)-1):
        temp[i] = Decimal(temp[i])
    if pos == 90:
        testing_set.append(temp)
        cases.append([training_set,testing_set])
        pos = 0
        training_set = []
        testing_set = []
    else:
        training_set.append(temp)
        pos += 1
    row = fr.readline()
fr.close()

n = len(cases)
u1 = KNN()
u2 = KNNFactory("MU_" + str(muid) + "_KNN").getKNN()
fw = open('w_results_mutant'+str(muid)+'.txt','w')
fw.write(str(n))
err_cases = {}
for i in range(n):
    u1.setInput(cases[i][0],cases[i][1])
    O1 = u1.getPredications()
    u2.setInput(cases[i][0],cases[i][1])
    O2 = u2.getPredications()
    if not (O1[0] == O2[0]):
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
    u2.setInput(cases[int(temp[0])][0],cases[int(temp[0])][1])
    O = u2.getPredications()
    u2.setInput(cases[int(temp[1])][0],cases[int(temp[1])][1])
    OO = u2.getPredications()
    if O[0] == OO[0]:
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
