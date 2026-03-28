from Risk_Formulas import *

def FAILTIM_cal(fname):
    fr = open(fname,'r')
    row = fr.readline()
    row = row.strip()
    temp = row.split(' ')
    n = int(temp[0])
    err_cases = {}
    for i in range(len(temp)-1):
        err_cases[temp[i+1]] = None

    case2MGs = [[] for i in range(n)]
    vMGs = {}
    row = fr.readline()
    while row:
        row = row.strip()
        temp = row.split(' ')
        mg = temp[0]+' '+temp[1]
        if temp[2] == '1':
            vMGs[mg] = None
        case2MGs[int(temp[0])].append(mg)
        case2MGs[int(temp[1])].append(mg)
        row = fr.readline()
    fr.close()

    u = RF()
    count = [0 for i in range(17)]
    for mg in vMGs:
        SMG = {}
        temp = mg.split(' ')
        cas0 = temp[0]
        cas1 = temp[1]
        for tmg in case2MGs[int(cas0)]:
            SMG[tmg] = None
        for tmg in case2MGs[int(cas1)]:
            SMG[tmg] = None
        
        spectrum = [[0,0,0,0],[0,0,0,0]]
        for tmg in SMG:
            temp = tmg.split(' ')
            if tmg in vMGs:
                if cas0 in temp:
                    spectrum[0][0] += 1
                else:
                    spectrum[0][2] += 1
                if cas1 in temp:
                    spectrum[1][0] += 1
                else:
                    spectrum[1][2] += 1
            else:
                if cas0 in temp:
                    spectrum[0][1] += 1
                else:
                    spectrum[0][3] += 1
                if cas1 in temp:
                    spectrum[1][1] += 1
                else:
                    spectrum[1][3] += 1

        for j in range(17):
            scores = []
            for i in range(2):
                a = spectrum[i][0]
                b = spectrum[i][1]
                c = spectrum[i][2]
                d = spectrum[i][3]
                scores.append(getattr(u,'rf'+str(j+1))(a,b,c,d))
            if scores[0] > scores[1]:
                if cas0 in err_cases:
                    count[j] += 1
            else:
                if cas1 in err_cases:
                    count[j] += 1

    print(fname)
    print(len(vMGs))
    print('======')
    for j in range(17):
        print(count[j])

    return count, len(vMGs)
