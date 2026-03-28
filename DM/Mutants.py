import math

class Mutants:
    def Origin(self, A, n):
        f1 = f2 = f3 = f4 = True
        for i in range(n):
            for j in range(n):
                if f1 and j > i and A[i * n + j] != 0:
                    f1 = False
                if f2 and i > j and A[i * n + j] != 0:
                    f2 = False
                if f3 and i+j < n-1 and A[i * n + j] != 0:
                    f3 = False
                if f4 and i+j > n-1 and A[i * n + j] != 0:
                    f4 = False
        if f1 or f2:
            result = 1
            for i in range(n):
                result *= A[i*n+i]
            return result
        elif f3 or f4:
            result = int(math.pow(-1, n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result
        else:
            return self.DeterComp(A, n)

    def Mutant1(self,A,n):
        f1 = f2 = f3 = f4 = True
        for i in range(n):
            for j in range(n):
                if (f1 and j>i and A[i*n+j] != 0):
                    f1 = False
                if (f2 and i>j and A[i*n+j] != 0):
                    f2 = False
                if (f3 and i+j<n-1 and A[i*n+j] != 0):
                    f3 = False
                if (f4 and i+j>n-1 and A[i*n+j] != 0):
                    f4 = False
        if (f1 or f2):
            result = 1
            for i in range(n):
                result += A[i*n+i]      # result *= A[i*n+i]  --> result += A[i*n+i]
            return result
        elif (f3 or f4):
            result = int(math.pow(-1, n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result
        else:
            return self.DeterComp(A, n)

    def Mutant2(self,A,n):
        f1 = f2 = f3 = f4 = True
        for i in range(n):
            for j in range(n):
                if (f1 and j>i and A[i*n+j] != 0):
                    f1 = False
                if (f2 and i>j and A[i*n+j] != 0):
                    f2 = False
                if (f3 and i+j<n-1 and A[i*n+j] != 0):
                    f3 = False
                if (f4 and i+j>n-1 and A[i*n+j] != 0):
                    f4 = False
        if (f1 or f2):
            result = 1
            for i in range(n):
                result *= A[i*n+i]
            return result
        elif (f3 or f4):
            result = int(math.pow(1,n*(n-1)/2))   # int(math.pow(-1,n*(n-1)/2))  -->  int(math.pow(1,n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result
        else:
            return self.DeterComp(A,n)

    def Mutant3(self,A,n):
        f1 = f2 = f3 = f4 = True
        for i in range(n):
            for j in range(n):
                if (f1 and j>i and A[i*n+j] != 0):
                    f1 = False
                if (f2 and i>j and A[i*n+j] != 0):
                    f2 = False
                if (f3 and i+j<n-1 and A[i*n+j] != 0):
                    f3 = False
                if (f4 and i+j>n-1 and A[i*n+j] != 0):
                    f4 = False
        if (f1 or f2):
            result = 1
            for i in range(n):
                result *= A[i*n]      # result *= A[i*n+i]  --> result *= A[i*n]
            return result
        elif (f3 or f4):
            result = int(math.pow(-1, n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result
        else:
            return self.DeterComp(A, n)

    def Mutant4(self,A,n):
        f1 = f2 = f3 = f4 = True
        for i in range(n):
            for j in range(n):
                if f1 and j>i and A[i * n + j] != 0:
                    f1 = False
                if f2 and i>j and A[i * n + j] != 0:
                    f2 = False
                if f3 and i+j<n-1 and A[i * n + j] != 0:
                    f3 = False
                if f4 and i+j>n-1 and A[i * n + j] != 0:
                    f4 = False
        if f1 or f2:
            result = 1
            for i in range(n):
                result *= A[i*n+1]      # result *= A[i*n+i]  --> result *= A[i*n+1]
            return result
        elif f3 or f4:
            result = int(math.pow(-1, n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result
        else:
            return self.DeterComp(A, n)

    def Mutant5(self,A,n):
        f1 = f2 = f3 = f4 = True
        for i in range(n):
            for j in range(n):
                if f1 and j>i and A[i * n + j] != 0:
                    f1 = False
                if f2 and i>j and A[i * n + j] != 0:
                    f2 = False
                if f3 and i+j<n-1 and A[i * n + j] != 0:
                    f3 = False
                if f4 and i+j>n-1 and A[i * n + j] != 0:
                    f4 = False
        if f1 or f2:
            result = 1
            for i in range(n):
                result *= A[i*n+i]
            return result
        elif f3 or f4:
            result = int(math.pow(-1, n*(n-1)/2))
            for i in range(n):
                result += A[i*n+(n-1-i)]  # result *= A[i*n+(n-1-i)]  --->  result += A[i*n+(n-1-i)]
            return result
        else:
            return self.DeterComp(A,n)

    def Mutant6(self, A, n):
        f1 = f2 = f3 = f4 = True
        for i in range(n):
            for j in range(n):
                if f1 and j > i and A[i * n + j] != 0:
                    f1 = False
                if f2 and i > j and A[i * n + j] != 0:
                    f2 = False
                if f3 and i+j < n-1 and A[i * n + j] != 0:
                    f3 = False
                if f4 and i+j > n-1 and A[i * n + j] != 0:
                    f4 = False
        if f1 or f2:
            result = 1
            for i in range(n):
                result *= A[i*n+i]
            return result
        elif f3 or f4:
            result = int(math.pow(-1, n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result
        else:
            return self.DeterComp2(A, n)

    def Mutant7(self, A, n):
        f1 = f2 = f3 = f4 = True
        for i in range(n):
            for j in range(n):
                if f1 and j > i and A[i * n + j] != 0:
                    f1 = False
                if f2 and i > j and A[i * n + j] != 0:
                    f2 = False
                if f3 and i+j < n-1 and A[i * n + j] != 0:
                    f3 = False
                if f4 and i+j > n-1 and A[i * n + j] != 0:
                    f4 = False
        if f1 or f2:
            result = 1
            for i in range(n):
                result *= A[i*n+i]
            return result
        elif f3 or f4:
            result = int(math.pow(-1, n*(n-1)/2))
            for i in range(n):
                result *= A[i*n+(n-1-i)]
            return result
        else:
            return self.DeterComp3(A, n)

    def DeterComp(self, A, n):
        mid = 0
        temp = []
        for i in range(n*n):
            temp.append(A[i])
        if n == 1:
            result = A[0]
        else:
            for i in range(n):
                mid += int(math.pow(-1, 2+i)) * A[i] * self.DeterComp(self.AlgComp(temp, n, i), n-1)
            result = mid
        return result

    def DeterComp2(self, A, n):
        mid = 0
        temp = []
        for i in range(n*n):
            temp.append(A[i])
        if (n == 1):
            result = A[0]
        else:
            for i in range(n):
                mid += int(math.pow(1, 2+i)) * A[i] * self.DeterComp2(self.AlgComp(temp,n,i),n-1)  # math.pow(-1,2+i)
            result = mid
        return result

    def DeterComp3(self, A, n):
        mid = 0
        temp = []
        for i in range(n*n):
            temp.append(A[i])
        if (n == 1):
            result = A[0]
        else:
            for i in range(n):
                mid *= int(math.pow(-1,2+i)) * A[i] * self.DeterComp3(self.AlgComp(temp,n,i),n-1)  # +=
            result = mid
        return result

    def AlgComp(self, x, n, i):
        array = []
        for j in range(n, n*n):
            if j % n == i:
                pass
            else:
                array.append(x[j])
        return array
