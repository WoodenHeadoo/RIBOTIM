
class RF:
    #Arithmetic Mean
    def rf1(self,a,b,c,d):
        if b==0 and c==0 and d==0:
            return 0.5
        else:
            return 2*(a*d-b*c)/((a+b)*(c+d)+(a+c)*(b+d))

    #Cohen
    def rf2(self,a,b,c,d):
        if b==0 and c==0 and d==0:
            return 0.5
        else:
            return 2*(a*d-b*c)/((a+b)*(b+d)+(a+c)*(c+d))

    #Fleiss
    def rf3(self,a,b,c,d):
        return 4*a*d-4*b*c-(b-c)*(b-c)

    #Scott
    def rf4(self,a,b,c,d):
        if b==0 and c==0 and d==0:
            return 0.5
        else:
            return (4*a*d-4*b*c-(b-c)*(b-c))/((2*a+b+c)*(b+c+2*d))

    #Rogot1
    def rf5(self,a,b,c,d):
        if b==0 and c==0 and d==0:
            return a/(2*a+b+c)
        else:
            return a/(2*a+b+c)+a/(b+c+2*d)

    #Kulczynski2
    def rf6(self,a,b,c,d):
        return a/(a+c)+a/(a+b)

    #Ochiai
    def rf7(self,a,b,c,d):
        return a*a/(a+b)

    #M2
    def rf8(self,a,b,c,d):
        return a/(a+2*b+2*c+d)

    #AMPLE2
    def rf9(self,a,b,c,d):
        return (2*a-1)/(2*a-1+b)

    #Naish2
    def rf10(self,a,b,c,d):
        return a-b/(b+d+1)

    #Jaccard, Anderberg, Sorensen-Dice, Dice, Goodman
    def rf11(self,a,b,c,d):
        return a/(a+b+c)

    #Tarantula, qe, CBIInc.
    def rf12(self,a,b,c,d):
        return a/(a+b)

    #Wong2, Hamann, Simple Matching, Sokal, R&T, Hamming, Euclid
    def rf13(self,a,b,c,d):
        return a+d

    #Wong1, R&R
    def rf14(self,a,b,c,d):
        return a

    #Naish1
    def rf15(self,a,b,c,d):
        if c > 0:
            return -1
        else:
            return d

    #Binary
    def rf16(self,a,b,c,d):
        if c > 0:
            return 0
        else:
            return 1

    #Wong3
    def rf17(self,a,b,c,d):
        if b <= 2:
            return a-b
        elif b <= 10:
            return a-2-0.1*(b-2)
        else:
            return a-2.8-0.001*(b-10)
