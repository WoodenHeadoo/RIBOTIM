
class MRs:
    def MRI1(self,I):
        O = [0]*9
        O[0] = I[3]
        O[1] = I[4]
        O[2] = I[5]
        O[3] = I[0]
        O[4] = I[1]
        O[5] = I[2]
        O[6] = I[6]
        O[7] = I[7]
        O[8] = I[8]
        return O

    def MRI2(self,I):
        O = [0]*9
        O[0] = I[0]-3*I[3]
        O[1] = I[1]-3*I[4]
        O[2] = I[2]-3*I[5]
        O[3] = I[3]
        O[4] = I[4]
        O[5] = I[5]
        O[6] = I[6]
        O[7] = I[7]
        O[8] = I[8]
        return O

    def MRI3(self,I):
        O = [0]*9
        O[0] = I[0]
        O[1] = I[3]
        O[2] = I[6]
        O[3] = I[1]
        O[4] = I[4]
        O[5] = I[7]
        O[6] = I[2]
        O[7] = I[5]
        O[8] = I[8]
        return O

    def MRI4(self,I):
        det = I[0]*I[4]*I[8]+I[1]*I[5]*I[6]+I[2]*I[3]*I[7]-I[0]*I[5]*I[7]-I[1]*I[3]*I[8]-I[2]*I[4]*I[6]
        if abs(det) < 1e-4:
            return None
        O = [0]*9
        O[0] = (I[4]*I[8]-I[5]*I[7])/det
        O[1] = (I[2]*I[7]-I[1]*I[8])/det
        O[2] = (I[1]*I[5]-I[2]*I[4])/det
        O[3] = (I[5]*I[6]-I[3]*I[8])/det
        O[4] = (I[0]*I[8]-I[2]*I[6])/det
        O[5] = (I[2]*I[3]-I[0]*I[5])/det
        O[6] = (I[3]*I[7]-I[4]*I[6])/det
        O[7] = (I[1]*I[6]-I[0]*I[7])/det
        O[8] = (I[0]*I[4]-I[1]*I[3])/det
        return O

    def MRI5(self,I):
        O = self.MRI1(I)
        O = self.MRI2(O)
        return O

    def MRI6(self,I):
        O = self.MRI2(I)
        O = self.MRI1(O)
        return O

    def MRI7(self,I):
        O = self.MRI1(I)
        O = self.MRI3(O)
        return O
    
    def MRI8(self,I):
        O = self.MRI3(I)
        O = self.MRI1(O)
        return O

    def MRI9(self,I):
        O = self.MRI2(I)
        O = self.MRI3(O)
        return O

    def MRI10(self,I):
        O = self.MRI3(I)
        O = self.MRI2(O)
        return O

    def MRO1(self,O1,O2):
        if abs(O1 + O2) < 1e-4:
            return True
        else:
            return False

    def MRO2(self,O1,O2):
        if abs(O1 - O2) < 1e-4:
            return True
        else:
            return False

    def MRO3(self,O1,O2):
        return self.MRO2(O1,O2)

    def MRO4(self,O1,O2):
        if abs(O1 * O2 - 1) < 1e-4:
            return True
        else:
            return False

    def MRO5(self,O1,O2):
        return self.MRO1(O1,O2)

    def MRO6(self,O1,O2):
        return self.MRO1(O1,O2)

    def MRO7(self,O1,O2):
        return self.MRO1(O1,O2)

    def MRO8(self,O1,O2):
        return self.MRO1(O1,O2)

    def MRO9(self,O1,O2):
        return self.MRO2(O1,O2)

    def MRO10(self,O1,O2):
        return self.MRO2(O1,O2)
