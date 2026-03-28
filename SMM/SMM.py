import sys

class SMM():
    def Normalization(self, n, m, c, ic, jc):
        result_c = []
        nz = 0
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(0)
            result_c.append(temp)
        for i in range(n):
            for j in range(ic[i], ic[i + 1]):
                result_c[i][jc[nz]] = c[nz]
                nz = nz + 1
        return result_c

    def SparseMatMul(self, n, m, a, ia, ja, b, ib, jb):
        nz = 0
        mask = []
        for i in range(m):
            mask.append(-1)
        c = []
        ic = [0]
        jc = []
        for i in range(n):
            ic.append(0)
        for i in range(n * m):
            c.append(0)
            jc.append(0)

        for i in range(0, n):
            for j in range(ia[i], ia[i + 1]):  # A的每行的非0值
                neighbour = ja[j]  # 哪一列
                aij = a[j]  # 具体值
                for k in range(ib[neighbour], ib[neighbour + 1]):  # B
                    icol_add = jb[k]
                    icol = mask[icol_add]
                    if icol == -1:
                        jc[nz] = icol_add
                        c[nz] = aij * b[k]
                        mask[icol_add] = nz
                        nz = nz + 1
                    else:
                        c[icol] = c[icol] + aij * b[k]
            for k in range(ic[i], nz):
                mask[jc[k]] = -1
            ic[i + 1] = nz
        c = c[:ic[-1]]
        jc = jc[:ic[-1]]
        C = self.Normalization(n, m, c, ic, jc)
        return C

    def CreateSparseMat(self, A):
        a = []
        ia = [0]
        ja = []
        off_set = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if not A[i][j] == 0:
                    a.append(A[i][j])
                    off_set = off_set + 1
                    ja.append(j)  # 只记录列
            ia.append(off_set)  # 前几行共有几个
        return a, ia, ja

    def MatMul(self, A, B):
        if not (len(A[0]) == len(B)):
            print("Matrix cannot product!\n Matrix production failure, since they do not match.")
            sys.exit(-1)
        product_row = len(A)
        product_col = len(B[0])
        (a, ia, ja) = self.CreateSparseMat(A)
        (b, ib, jb) = self.CreateSparseMat(B)
        C = self.SparseMatMul(product_row, product_col, a, ia, ja, b, ib, jb)
        return C

class MU_1_SMM(SMM):
    def SparseMatMul(self, n, m, a, ia, ja, b, ib, jb):
        nz = 0
        mask = []
        for i in range(m):
            mask.append(-1)
        c = []
        ic = [0]
        jc = []
        for i in range(n):
            ic.append(0)
        for i in range(n * m):
            c.append(0)
            jc.append(0)

        for i in range(0, n):
            for j in range(ia[i], ia[i + 1]):
                neighbour = ja[j]
                aij = a[j]
                for k in range(ib[neighbour], ib[neighbour + 1]):
                    icol_add = jb[k]
                    icol = mask[icol_add]
                    if (icol == -1):
                        jc[nz] = icol_add
                        c[nz] = aij * b[k]
                        mask[icol_add] = nz
                        # nz = nz + 1
                    else:
                        c[icol] = c[icol] + aij * b[k]
            for k in range(ic[i], nz):
                mask[jc[k]] = -1
            ic[i + 1] = nz
        c = c[:ic[-1]]
        jc = jc[:ic[-1]]
        C = self.Normalization(n, m, c, ic, jc)
        return C

class MU_2_SMM(SMM):
    def SparseMatMul(self, n, m, a, ia, ja, b, ib, jb):
        nz = 0
        mask = []
        for i in range(m):
            mask.append(-1)
        c = []
        ic = [0]
        jc = []
        for i in range(n):
            ic.append(0)
        for i in range(n * m):
            c.append(0)
            jc.append(0)

        for i in range(0, n):
            for j in range(ia[i], ia[i + 1]):
                neighbour = ja[j]
                aij = a[j]
                for k in range(ib[neighbour], ib[neighbour + 1]):
                    icol_add = jb[k]
                    icol = mask[icol_add]
                    if (icol == -1):
                        jc[nz] = icol_add
                        c[nz] = b[k]  # c[nz] = aij * b[k]
                        mask[icol_add] = nz
                        nz = nz + 1
                    else:
                        c[icol] = c[icol] + aij * b[k]
            for k in range(ic[i], nz):
                mask[jc[k]] = -1
            ic[i + 1] = nz
        c = c[:ic[-1]]
        jc = jc[:ic[-1]]
        C = self.Normalization(n, m, c, ic, jc)
        return C

class MU_3_SMM(SMM):
    def SparseMatMul(self, n, m, a, ia, ja, b, ib, jb):
        nz = 0
        mask = []
        for i in range(m):
            mask.append(-1)
        c = []
        ic = [0]
        jc = []
        for i in range(n):
            ic.append(0)
        for i in range(n * m):
            c.append(0)
            jc.append(0)

        for i in range(0, n):
            for j in range(ia[i], ia[i + 1]):
                neighbour = ja[j]
                aij = a[j]
                for k in range(ib[neighbour], ib[neighbour + 1]):
                    icol_add = jb[k]
                    icol = mask[icol_add]
                    if (icol == -1):
                        jc[nz] = icol_add
                        c[nz] = aij  # c[nz] = aij * b[k]
                        mask[icol_add] = nz
                        nz = nz + 1
                    else:
                        c[icol] = c[icol] + aij * b[k]
            for k in range(ic[i], nz):
                mask[jc[k]] = -1
            ic[i + 1] = nz
        c = c[:ic[-1]]
        jc = jc[:ic[-1]]
        C = self.Normalization(n, m, c, ic, jc)
        return C

class MU_4_SMM(SMM):
    def SparseMatMul(self, n, m, a, ia, ja, b, ib, jb):
        nz = 0
        mask = []
        for i in range(m):
            mask.append(-1)
        c = []
        ic = [0]
        jc = []
        for i in range(n):
            ic.append(0)
        for i in range(n * m):
            c.append(0)
            jc.append(0)

        for i in range(0, n):
            for j in range(ia[i], ia[i + 1]):
                neighbour = ja[j]
                aij = a[j]
                for k in range(ib[neighbour], ib[neighbour + 1]):
                    icol_add = jb[k]
                    icol = mask[icol_add]
                    if icol == -1:
                        jc[nz] = icol_add
                        c[nz] = aij * b[k]
                        mask[icol_add] = nz
                        nz = nz + 1
                    else:
                        # 只要a和b中含有两个或两个以上非0数对，执行此行代码
                        c[icol] = c[icol] + aij  # c[icol] = c[icol]+aij*b[k]
            for k in range(ic[i], nz):
                mask[jc[k]] = -1
            ic[i + 1] = nz
        c = c[:ic[-1]]
        jc = jc[:ic[-1]]
        C = self.Normalization(n, m, c, ic, jc)
        return C

class MU_5_SMM(SMM):
    def SparseMatMul(self, n, m, a, ia, ja, b, ib, jb):
        nz = 0
        mask = []
        for i in range(m):
            mask.append(-1)
        c = []
        ic = [0]
        jc = []
        for i in range(n):
            ic.append(0)
        for i in range(n * m):
            c.append(0)
            jc.append(0)

        for i in range(0, n):
            for j in range(ia[i], ia[i + 1]):
                neighbour = ja[j]
                aij = a[j]
                for k in range(ib[neighbour], ib[neighbour + 1]):
                    icol_add = jb[k]
                    icol = mask[icol_add]
                    if (icol == -1):
                        jc[nz] = icol_add
                        c[nz] = aij * b[k]
                        mask[icol_add] = nz
                        nz = nz + 1
                    else:
                        c[icol] = c[icol] + b[k]  # c[icol] = c[icol]+aij*b[k]
            for k in range(ic[i], nz):
                mask[jc[k]] = -1
            ic[i + 1] = nz
        c = c[:ic[-1]]
        jc = jc[:ic[-1]]
        C = self.Normalization(n, m, c, ic, jc)
        return C

class MU_6_SMM(SMM):
    def SparseMatMul(self, n, m, a, ia, ja, b, ib, jb):
        nz = 0
        mask = []
        for i in range(m):
            mask.append(-1)
        c = []
        ic = [0]
        jc = []
        for i in range(n):
            ic.append(0)
        for i in range(n * m):
            c.append(0)
            jc.append(0)

        for i in range(0, n):
            for j in range(ia[i], ia[i + 1]):
                neighbour = ja[j]
                aij = a[j]
                for k in range(ib[neighbour], ib[neighbour + 1]):
                    icol_add = jb[k]
                    icol = mask[icol_add]
                    if (icol == -1):
                        jc[nz] = icol_add
                        c[nz] = aij * b[k]
                        mask[icol_add] = nz
                        nz = nz + 1
                    else:
                        c[icol] = c[icol] + aij + b[k]  # this line is modified from " aij*b[k]"
            for k in range(ic[i], nz):
                mask[jc[k]] = -1
            ic[i + 1] = nz
        c = c[:ic[-1]]
        jc = jc[:ic[-1]]
        C = self.Normalization(n, m, c, ic, jc)
        return C

class MU_7_SMM(SMM):
    def SparseMatMul(self, n, m, a, ia, ja, b, ib, jb):
        nz = 0
        mask = []
        for i in range(m):
            mask.append(-1)
        c = []
        ic = [0]
        jc = []
        for i in range(n):
            ic.append(0)
        for i in range(n * m):
            c.append(0)
            jc.append(0)

        for i in range(0, n):
            for j in range(ia[i], ia[i + 1]):
                neighbour = ja[j]
                aij = a[j]
                for k in range(ib[neighbour], ib[neighbour + 1]):
                    icol_add = jb[k]
                    icol = mask[icol_add]
                    if (icol == -1):
                        jc[nz] = icol_add
                        c[nz] = aij * b[k]
                        mask[icol_add] = nz
                        nz = nz + 1
                    else:
                        c[icol] = c[icol] + aij * b[k]
            for k in range(ic[i], nz):
                mask[jc[i]] = -1  # this line is modified from jc[k]
            ic[i + 1] = nz
        c = c[:ic[-1]]
        jc = jc[:ic[-1]]
        C = self.Normalization(n, m, c, ic, jc)
        return C

class SMMFactory:
    def __init__(self, class_id):
        self.class_id = class_id

    def getSMM(self):
        if (self.class_id == 1):
            return MU_1_SMM()
        elif (self.class_id == 2):
            return MU_2_SMM()
        elif (self.class_id == 3):
            return MU_3_SMM()
        elif (self.class_id == 4):
            return MU_4_SMM()
        elif (self.class_id == 5):
            return MU_5_SMM()
        elif (self.class_id == 6):
            return MU_6_SMM()
        elif (self.class_id == 7):
            return MU_7_SMM()
        else:
            return SMM()
