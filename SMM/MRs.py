import math

def Normalization(n, m, c, ic, jc):
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

def SparseMatMul(n, m, a, ia, ja, b, ib, jb):
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
                if icol == -1:  # 为什么会有这么一个分支, 这个分支是一定经过的
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
    C = Normalization(n, m, c, ic, jc)
    return C

def CreateSparseMat(A):
    a = []
    ia = [0]  # 为什么？
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

def MatMul(A, B):
    if not (len(A[0]) == len(B)):
        print("Matrix cannot product!\n Matrix production failure, since they do not match.")
        sys.exit(-1)
    product_row = len(A)
    product_col = len(B[0])
    (a, ia, ja) = CreateSparseMat(A)
    (b, ib, jb) = CreateSparseMat(B)
    C = SparseMatMul(product_row, product_col, a, ia, ja, b, ib, jb)
    return C

def mat_transpose(A):
    row = len(A)
    column = len(A[0])
    B = []
    for i in range(column):
        temp = []
        for j in range(0, row):
            temp.append(A[j][i])
        B.append(temp)
    return B

def mat_copy(A):
    B = []
    for i in range(len(A)):
        temp = []
        for j in range(len(A[0])):
            temp.append(A[i][j])
        B.append(temp)
    return B

def AssertMRViolation(ftc_output, ftc_expected_output):
    d = 0.00001
    row = len(ftc_expected_output)
    col = len(ftc_expected_output[0])
    if not (row == len(ftc_output) and col == len(ftc_output[0])):
        return True
    for i in range(row):
        for j in range(col):
            if math.fabs(ftc_output[i][j] - ftc_expected_output[i][j]) >= d:
                return True
    return False

def getIdentityMatrix(dim):
    I = []
    for i in range(dim):
        temp = []
        for j in range(dim):
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        I.append(temp)
    return I

def getPMatrix(dim):
    if dim < 2:
        print("Cannot compound, since matrix has less than two rows!")
        sys.exit(-1)
    P = getIdentityMatrix(dim)
    temp = P[0]
    P[0] = P[1]
    P[1] = temp
    return P

def getQMatrix(dim, constant):
    Q = []
    for i in range(dim):
        temp = []
        for j in range(dim):
            if i == j:
                temp.append(constant)
            else:
                temp.append(0)
        Q.append(temp)
    return Q

def mat_multiple_constant(matrix, scalar):
    scaled_matrix = mat_copy(matrix)
    for i in range(len(scaled_matrix)):
        for j in range(len(scaled_matrix[0])):
            scaled_matrix[i][j] = scaled_matrix[i][j] * scalar
    return scaled_matrix

def mat_addition(A, B):
    C = []
    if not (len(A) == len(B) and len(A[0]) == len(B[0])):
        print("Can not compound!\n Matrix addition failure, since they do not have the same dimension.")
        sys.exit(-1)
    for i in range(len(A)):
        temp = []
        for j in range(len(A[0])):
            temp.append(A[i][j] + B[i][j])
        C.append(temp)
    return C

class MRs:
    def MRI1(self, otc_A, otc_B):
        ftc_A = mat_transpose(otc_B)
        ftc_B = mat_transpose(otc_A)
        return ftc_A, ftc_B

    def MRO1(self, otc_A, otc_B, ori_output, mrs_output):
        ftc_expected_output = mat_transpose(ori_output)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI2(self, otc_A, otc_B):
        P = getPMatrix(len(otc_A))
        ftc_A = MatMul(P, otc_A)
        ftc_B = mat_copy(otc_B)
        return ftc_A, ftc_B

    def MRO2(self, otc_A, otc_B, ori_output, mrs_output):
        P = getPMatrix(len(otc_A))
        ftc_expected_output = MatMul(P, ori_output)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI3(self, otc_A, otc_B):
        P = getPMatrix(len(otc_B[0]))
        ftc_A = mat_copy(otc_A)
        ftc_B = MatMul(otc_B, P)
        return ftc_A, ftc_B

    def MRO3(self, otc_A, otc_B, ori_output, mrs_output):
        P = getPMatrix(len(otc_B[0]))
        ftc_expected_output = MatMul(ori_output, P)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI4(self, otc_A, otc_B):
        Q = getQMatrix(len(otc_A), 3)
        ftc_A = MatMul(Q, otc_A)
        ftc_B = mat_copy(otc_B)
        return ftc_A, ftc_B

    def MRO4(self, otc_A, otc_B, ori_output, mrs_output):
        Q = getQMatrix(len(otc_A), 3)
        ftc_expected_output = MatMul(Q, ori_output)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI5(self, otc_A, otc_B):
        Q = getQMatrix(len(otc_A), 4)
        ftc_B = MatMul(otc_B, Q)
        ftc_A = mat_copy(otc_A)
        return ftc_A, ftc_B

    def MRO5(self, otc_A, otc_B, ori_output, mrs_output):
        Q = getQMatrix(len(otc_A), 4)
        ftc_expected_output = MatMul(ori_output, Q)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI6(self, otc_A, otc_B):
        scalar = 6
        ftc_A = mat_multiple_constant(otc_A, scalar)
        ftc_B = mat_copy(otc_B)
        return ftc_A, ftc_B

    def MRO6(self, otc_A, otc_B, ori_output, mrs_output):
        scalar = 6
        ftc_expected_output = mat_multiple_constant(ori_output, scalar)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI7(self, otc_A, otc_B):
        scalar = 7
        ftc_B = mat_multiple_constant(otc_B, scalar)
        ftc_A = mat_copy(otc_A)
        return ftc_A, ftc_B

    def MRO7(self, otc_A, otc_B, ori_output, mrs_output):
        scalar = 7
        ftc_expected_output = mat_multiple_constant(ori_output, scalar)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI8(self, otc_A, otc_B):
        dim = len(otc_A)
        I = getIdentityMatrix(dim)
        ftc_A = mat_addition(otc_A, I)
        ftc_B = mat_copy(otc_B)
        return ftc_A, ftc_B

    def MRO8(self, otc_A, otc_B, ori_output, mrs_output):
        ftc_expected_output = mat_addition(ori_output, otc_B)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI9(self, otc_A, otc_B):
        dim = len(otc_B)
        I = getIdentityMatrix(dim)
        ftc_A = mat_copy(otc_A)
        ftc_B = mat_addition(otc_B, I)
        return ftc_A, ftc_B

    def MRO9(self, otc_A, otc_B, ori_output, mrs_output):
        ftc_expected_output = mat_addition(otc_A, ori_output)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI10(self, otc_A, otc_B):
        ftc_A = mat_transpose(otc_B)
        ftc_B = mat_transpose(otc_A)
        P = getPMatrix(len(ftc_A))
        ftc_A = MatMul(P, ftc_A)
        return ftc_A, ftc_B

    def MRO10(self, otc_A, otc_B, ori_output, mrs_output):
        P = getPMatrix(len(otc_B[0]))
        ftc_expected_output = MatMul(P, mat_transpose(ori_output))
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI11(self, otc_A, otc_B):
        ftc_A = mat_transpose(otc_B)
        ftc_B = mat_transpose(otc_A)
        P = getPMatrix(len(ftc_B[0]))
        ftc_B = MatMul(ftc_B, P)
        return ftc_A, ftc_B

    def MRO11(self, otc_A, otc_B, ori_output, mrs_output):
        P = getPMatrix(len(otc_A))
        ftc_expected_output = MatMul(mat_transpose(ori_output), P)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI12(self, otc_A, otc_B):
        P = getPMatrix(len(otc_A))
        temp = MatMul(P, otc_A)
        ftc_B = mat_transpose(temp)
        ftc_A = mat_transpose(otc_B)
        return ftc_A, ftc_B

    def MRO12(self, otc_A, otc_B, ori_output, mrs_output):
        P = getPMatrix(len(otc_A))
        ftc_expected_output = MatMul(mat_transpose(ori_output), P)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI13(self, otc_A, otc_B):
        P1 = getPMatrix(len(otc_A))
        P2 = getPMatrix(len(otc_B[0]))
        ftc_A = MatMul(P1, otc_A)
        ftc_B = MatMul(otc_B, P2)
        return ftc_A, ftc_B

    def MRO13(self, otc_A, otc_B, ori_output, mrs_output):
        P1 = getPMatrix(len(otc_A))
        P2 = getPMatrix(len(otc_B[0]))
        ftc_expected_output = MatMul(MatMul(P1, ori_output), P2)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI14(self, otc_A, otc_B):
        P = getPMatrix(len(otc_B[0]))
        temp = MatMul(otc_B, P)
        ftc_A = mat_transpose(temp)
        ftc_B = mat_transpose(otc_A)
        return ftc_A, ftc_B

    def MRO14(self, otc_A, otc_B, ori_output, mrs_output):
        P = getPMatrix(len(otc_B[0]))
        ftc_expected_output = MatMul(P, mat_transpose(ori_output))
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True

    def MRI15(self, otc_A, otc_B):
        P1 = getPMatrix(len(otc_B[0]))
        P2 = getPMatrix(len(otc_A))
        ftc_A = MatMul(P2, otc_A)
        ftc_B = MatMul(otc_B, P1)
        return ftc_A, ftc_B

    def MRO15(self, otc_A, otc_B, ori_output, mrs_output):
        P1 = getPMatrix(len(otc_B[0]))
        P2 = getPMatrix(len(otc_A))
        ftc_expected_output = MatMul(MatMul(P2, ori_output), P1)
        violation = AssertMRViolation(ftc_expected_output, mrs_output)
        if violation:
            return False
        else:
            return True
