import math

def ribotim(fname,iters=10000,c1=1.0,c2=1.5,eta=0.2):
    fr = open(fname,'r')
    row = fr.readline()
    row = row.strip()
    temp = row.split(' ')
    n = int(temp[0])
    err_cases = {}
    for i in range(len(temp)-1):
        err_cases[int(temp[i+1])] = None

    vMGs = [[] for i in range(n)]
    sMGs = [[] for i in range(n)]
    spectrum = [[0,0,0,0] for i in range(n)]
    num_sat = 0
    num_vio = 0
    vvMGs = {}
    row = fr.readline()
    while row:
        row = row.strip()
        temp = row.split(' ')
        if temp[2] == '1':
            vMGs[int(temp[0])].append(int(temp[1]))
            vMGs[int(temp[1])].append(int(temp[0]))
            spectrum[int(temp[0])][2] -= 1
            spectrum[int(temp[0])][0] += 1
            spectrum[int(temp[1])][2] -= 1
            spectrum[int(temp[1])][0] += 1
            num_vio += 1
            vvMGs[temp[0]+' '+temp[1]] = None
        else:
            sMGs[int(temp[0])].append(int(temp[1]))
            sMGs[int(temp[1])].append(int(temp[0]))
            spectrum[int(temp[0])][3] -= 1
            spectrum[int(temp[0])][1] += 1
            spectrum[int(temp[1])][3] -= 1
            spectrum[int(temp[1])][1] += 1
            num_sat += 1
        row = fr.readline()
    fr.close()

    scores = {}
    for i in range(n):
        spectrum[i][2] += num_vio
        spectrum[i][3] += num_sat
        a = spectrum[i][0]
        b = spectrum[i][1]
        c = spectrum[i][2]
        d = spectrum[i][3]
        scores[i] = a/(a+c)-b/(b+d)
    ma = max(scores)
    mi = min(scores)
    for i in range(n):
        scores[i] = 2*(scores[i]-mi)/(ma-mi)-1
        #scores[i] = 0

    for mm in range(iters):
        rs = []
        for i in range(n):
            rs.append(1.0/(1+math.exp(-1.0*scores[i])))
        for i in range(n):
            for j in vMGs[i]:
                #temp = (1-c1*rs[j])*rs[i]*(1-rs[i])/(rs[i]+rs[j]-c1*rs[i]*rs[j])
                temp = (1-c1*rs[j])*rs[i]*(1-rs[i])*(1-rs[i]-rs[j]+c1*rs[i]*rs[j])
                scores[i] += eta*temp*2*num_sat/(num_sat+num_vio)
            for j in sMGs[i]:
                #temp = (1-c2*rs[j])*rs[i]*(1-rs[i])/(rs[i]+rs[j]-c2*rs[i]*rs[j]-1)
                temp = (1-c2*rs[j])*rs[i]*(1-rs[i])*(-rs[i]-rs[j]+c2*rs[i]*rs[j])
                scores[i] += eta*temp*2*num_vio/(num_sat+num_vio)

    count = 0
    sc_p = {}
    for mg in vvMGs:
        temp = mg.split(' ')
        cas0 = int(temp[0])
        cas1 = int(temp[1])
        sc_p[cas0] = scores[cas0]
        sc_p[cas1] = scores[cas1]
        if scores[cas0] > scores[cas1]:
            if cas0 in err_cases:
                count += 1
        else:
            if cas1 in err_cases:
                count += 1
    print(fname)
    print(str(count)+'/'+str(len(vvMGs)))

    sc_p = sorted(sc_p.items(),key=lambda x:x[1],reverse=True)
    k = [1,5,10,len(sc_p)]
    for j in range(len(k)):
        dcg = 0.0
        idcg = 0.0
        for i in range(k[j]):
            if (i < len(sc_p)) and (sc_p[i][0] in err_cases):
                dcg += 1.0/math.log(i+2,2)
            if i < len(err_cases):
                idcg += 1.0/math.log(i+2,2)
        print('NDCG@'+str(k[j])+': '+str(dcg/idcg))

    return count, len(vvMGs)
