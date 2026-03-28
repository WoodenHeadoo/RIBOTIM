import math

class MRs:
    def MRI1(self, argv):
        a = argv[0]
        b = argv[1]
        c = argv[2]
        a1 = math.sqrt(2 * pow(b, 2) + 2 * pow(c, 2) - pow(a, 2))
        b1 = b
        c1 = c
        edge = [a1, b1, c1]
        return edge

    def MRI2(self, argv):
        a = argv[0]
        b = argv[1]
        c = argv[2]
        a1 = a
        b1 = math.sqrt(2 * pow(a, 2) + 2 * pow(c, 2) - pow(b, 2))
        c1 = c
        edge = [a1, b1, c1]
        return edge

    def MRI3(self, argv):
        a = argv[0]
        b = argv[1]
        c = argv[2]
        a1 = a
        b1 = b
        c1 = math.sqrt(2 * pow(a, 2) + 2 * pow(b, 2) - pow(c, 2))
        edge = [a1, b1, c1]
        return edge

    def MRI4(self, argv):
        a = argv[0]
        b = argv[1]
        c = argv[2]
        a1 = math.sqrt(2 * pow(b, 2) + 2 * pow(c, 2) - pow(a, 2))
        b1 = math.sqrt(3 * pow(b, 2) + 6 * pow(c, 2) - 2 * pow(a, 2))
        c1 = c
        edge = [a1, b1, c1]
        return edge

    def MRI5(self, argv):
        a = argv[0]
        b = argv[1]
        c = argv[2]
        a1 = math.sqrt(2 * pow(b, 2) + 2 * pow(c, 2) - pow(a, 2))
        b1 = b
        c1 = math.sqrt(6 * pow(b, 2) + 3 * pow(c, 2) - 2 * pow(a, 2))
        edge = [a1, b1, c1]
        return edge

    def MRI6(self, argv):
        a = argv[0]
        b = argv[1]
        c = argv[2]
        a1 = math.sqrt(3 * pow(a, 2) + 6 * pow(c, 2) - 2 * pow(b, 2))
        b1 = math.sqrt(2 * pow(a, 2) + 2 * pow(c, 2) - pow(b, 2))
        c1 = c
        edge = [a1, b1, c1]
        return edge

    def MRI7(self, argv):
        a = argv[0]
        b = argv[1]
        c = argv[2]
        a1 = math.sqrt(3 * pow(a, 2) + 6 * pow(b, 2) - 2 * pow(c, 2))
        b1 = b
        c1 = math.sqrt(2 * pow(a, 2) + 2 * pow(b, 2) - pow(c, 2))
        edge = [a1, b1, c1]
        return edge

    def MRI8(self, argv):
        a = argv[0]
        b = argv[1]
        c = argv[2]
        a1 = a
        b1 = math.sqrt(2 * pow(a, 2) + 2 * pow(c, 2) - pow(b, 2))
        c1 = math.sqrt(6 * pow(a, 2) + 3 * pow(c, 2) - 2 * pow(b, 2))
        edge = [a1, b1, c1]
        return edge

    def MRI9(self, argv):
        a = argv[0]
        b = argv[1]
        c = argv[2]
        a1 = a
        b1 = math.sqrt(6 * pow(a, 2) + 3 * pow(b, 2) - 2 * pow(c, 2))
        c1 = math.sqrt(2 * pow(a, 2) + 2 * pow(b, 2) - pow(c, 2))
        edge = [a1, b1, c1]
        return edge

    def MRO(self, s, s1):
        s = float('%.4f' % s)
        s1 = float('%.4f' % s1)
        if abs(s1 - s) < 1e-4:
            return True
        else:
            return False
