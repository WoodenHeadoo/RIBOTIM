from TCAS import *

class MRs:
    def MR1(self,argv):
        o_s = TCAS().Tcas(argv)
        argv_f = argv.copy()
        if o_s == 'UPWARD_RA':
            argv_f[3] = ((argv[3] + argv[5]) / 2) - 1
            argv_f[5] = ((argv[3] + argv[5]) / 2) + 1
        elif o_s == 'DOWNWARD_RA':
            argv_f[3] = ((argv[3] + argv[5]) / 2) + 1
            argv_f[5] = ((argv[3] + argv[5]) / 2) - 1
        elif o_s == 'UNRESOLVED':
            argv_f[3] = ((argv[3] + argv[5]) / 2)
            argv_f[5] = ((argv[3] + argv[5]) / 2)
        return argv_f

    def MR2(self,argv):
        o_s = TCAS().Tcas(argv)
        argv_f = argv.copy()
        if o_s == 'UPWARD_RA':
            argv_f[8] = argv[8] - 10
        elif o_s == 'DOWNWARD_RA':
            argv_f[7] = argv[7] + 10  # y8>x8
            if argv[11] == 1:
                argv_f[8] = argv_f[7] + 110  # y8+100<=y9
            else:
                argv_f[8] = argv_f[7] + 10  # y8<=y9
        elif o_s == 'UNRESOLVED':
            argv_f[7] = argv[7] - 10  # y8<x8
            argv_f[8] = argv[8] + 10  # y9>x9
            if argv[11] == 1:
                if argv[7] > (argv[8] - 100):  # x8>x9-100
                    argv_f[8] = argv_f[7] + 90  # y8>y9-100
                elif argv[7] == (argv[8] - 100):
                    return argv_f
                else:
                    argv_f[8] = argv_f[7] + 110
            else:
                if argv[7] > argv[8]:
                    argv_f[7] = argv_f[8] + 1
                elif argv[7] == argv[8]:  # 无解
                    return argv_f
                else:
                    argv_f[8] = argv_f[7] + 1
        return argv_f

    def MR3(self,argv):
        o_s = TCAS().Tcas(argv)
        argv_f = argv.copy()
        if o_s == 'UPWARD_RA':
            if argv[6] == 3:
                return argv_f
            else:
                argv_f[6] = argv[6] + 1
        elif o_s == 'DOWNWARD_RA':
            if argv[6] == 0:
                return argv_f
            else:
                argv_f[6] = argv[6] - 1
        elif o_s == 'UNRESOLVED':
            if argv[3] <= argv[5]:
                if argv[6] == 0:
                    return argv_f
                else:
                    argv_f[6] = argv[6] - 1
            else:
                if argv[6] == 3:
                    return argv_f
                else:
                    argv_f[6] = argv[6] + 1
        return argv_f

    def MR4(self,argv):
        o_s = TCAS().Tcas(argv)
        argv_f = argv.copy()
        argv_ff = argv_f.copy()
        if o_s == 'UPWARD_RA':
            argv_f[3] = ((argv[3] + argv[5]) / 2) - 1
            argv_f[5] = ((argv[3] + argv[5]) / 2) + 1
            argv_ff = argv_f.copy()
            argv_ff[8] = argv_f[8] - 10
        elif o_s == 'DOWNWARD_RA':
            argv_f[3] = ((argv[3] + argv[5]) / 2) + 1
            argv_f[5] = ((argv[3] + argv[5]) / 2) - 1
            argv_ff = argv_f.copy()
            argv_ff[7] = argv_f[7] + 10  # y8>x8
            if argv_f[11] == 1:
                argv_ff[8] = argv_ff[7] + 110  # y8+100<=y9
            else:
                argv_ff[8] = argv_ff[7] + 10  # y8<=y9
        elif o_s == 'UNRESOLVED':
            argv_f[3] = ((argv[3] + argv[5]) / 2)
            argv_f[5] = ((argv[3] + argv[5]) / 2)
            argv_ff = argv_f.copy()
            argv_ff[7] = argv_f[7] - 10  # y8<x8
            argv_ff[8] = argv_f[8] + 10  # y9>x9
            if argv_f[11] == 1:
                if argv_f[7] > (argv_f[8] - 100):  # x8>x9-100
                    argv_ff[8] = argv_ff[7] + 90  # y8>y9-100
                elif argv_f[7] == (argv_f[8] - 100):
                    return argv_ff
                else:
                    argv_ff[8] = argv_ff[7] + 110
            else:
                if argv_f[7] > argv_f[8]:
                    argv_ff[7] = argv_ff[8] + 1
                elif argv_f[7] == argv_f[8]:  # 无解
                    return argv_ff
                else:
                    argv_ff[8] = argv_ff[7] + 1
        return argv_ff

    def MR5(self,argv):
        o_s = TCAS().Tcas(argv)
        argv_f = argv.copy()
        argv_ff = argv_f.copy()
        if o_s == 'UPWARD_RA':
            argv_f[3] = ((argv[3] + argv[5]) / 2) - 1
            argv_f[5] = ((argv[3] + argv[5]) / 2) + 1
            argv_ff = argv_f.copy()
            if argv_f[6] == 3:
                return argv_ff
            else:
                argv_ff[6] = argv_f[6] + 1
        elif o_s == 'DOWNWARD_RA':
            argv_f[3] = ((argv[3] + argv[5]) / 2) + 1
            argv_f[5] = ((argv[3] + argv[5]) / 2) - 1
            argv_ff = argv_f.copy()
            if argv_f[6] == 0:
                return argv_ff
            else:
                argv_ff[6] = argv_f[6] - 1
        elif o_s == 'UNRESOLVED':
            argv_f[3] = ((argv[3] + argv[5]) / 2)
            argv_f[5] = ((argv[3] + argv[5]) / 2)
            argv_ff = argv_f.copy()
            if argv_f[3] <= argv_f[5]:
                if argv_f[6] == 0:
                    return argv_ff
                else:
                    argv_ff[6] = argv_f[6] - 1
            else:
                if argv_f[6] == 3:
                    return argv_ff
                else:
                    argv_ff[6] = argv_f[6] + 1
        return argv_ff

    def MR6(self,argv):
        o_s = TCAS().Tcas(argv)
        argv_f = argv.copy()
        argv_ff = argv_f.copy()
        if o_s == 'UPWARD_RA':
            argv_f[8] = argv[8] - 10
            argv_ff = argv_f.copy()
            argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2) - 1
            argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2) + 1
        elif o_s == 'DOWNWARD_RA':
            argv_f[7] = argv[7] + 10  # y8>x8
            if argv[11] == 1:
                argv_f[8] = argv_f[7] + 110  # y8+100<=y9
            else:
                argv_f[8] = argv_f[7] + 10  # y8<=y9
            argv_ff = argv_f.copy()
            argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2) + 1
            argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2) - 1
        elif o_s == 'UNRESOLVED':
            argv_f[7] = argv[7] - 10  # y8<x8
            argv_f[8] = argv[8] + 10  # y9>x9
            if argv[11] == 1:
                if argv[7] > (argv[8] - 100):  # x8>x9-100
                    argv_f[8] = argv_f[7] + 90  # y8>y9-100
                elif argv[7] == (argv[8] - 100):
                    return argv_ff
                else:
                    argv_f[8] = argv_f[7] + 110
            else:
                if argv[7] > argv[8]:
                    argv_f[7] = argv_f[8] + 1
                elif argv[7] == argv[8]:  # 无解
                    return argv_ff
                else:
                    argv_f[8] = argv_f[7] + 1
            argv_ff = argv_f.copy()
            argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2)
            argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2)
        return argv_ff

    def MR7(self,argv):
        o_s = TCAS().Tcas(argv)
        argv_f = argv.copy()
        argv_ff = argv_f.copy()
        if o_s == 'UPWARD_RA':
            if argv[6] == 3:
                return argv_f
            else:
                argv_f[6] = argv[6] + 1
            argv_ff = argv_f.copy()
            argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2) - 1
            argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2) + 1
        elif o_s == 'DOWNWARD_RA':
            if argv[6] == 0:
                return argv_ff
            else:
                argv_f[6] = argv[6] - 1
            argv_ff = argv_f.copy()
            argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2) + 1
            argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2) - 1
        elif o_s == 'UNRESOLVED':
            if argv[3] <= argv[5]:
                if argv[6] == 0:
                    return argv_ff
                else:
                    argv_f[6] = argv[6] - 1
            else:
                if argv[6] == 3:
                    return argv_ff
                else:
                    argv_f[6] = argv[6] + 1
            argv_ff = argv_f.copy()
            argv_ff[3] = ((argv_f[3] + argv_f[5]) / 2)
            argv_ff[5] = ((argv_f[3] + argv_f[5]) / 2)
        return argv_ff

    def MR8(self,argv):
        o_s = TCAS().Tcas(argv)
        argv_f = argv.copy()
        argv_ff = argv_f.copy()
        if o_s == 'UPWARD_RA':
            argv_f[8] = argv[8] - 10
            argv_ff = argv_f.copy()
            if argv_f[6] == 3:
                return argv_ff
            else:
                argv_ff[6] = argv_f[6] + 1
        elif o_s == 'DOWNWARD_RA':
            argv_f[7] = argv[7] + 10  # y8>x8
            if argv[11] == 1:
                argv_f[8] = argv_f[7] + 110  # y8+100<=y9
            else:
                argv_f[8] = argv_f[7] + 10  # y8<=y9
            argv_ff = argv_f.copy()
            if argv_f[6] == 0:
                return argv_ff
            else:
                argv_ff[6] = argv_f[6] - 1
        elif o_s == 'UNRESOLVED':
            argv_f[7] = argv[7] - 10  # y8<x8
            argv_f[8] = argv[8] + 10  # y9>x9
            if argv[11] == 1:
                if argv[7] > (argv[8] - 100):  # x8>x9-100
                    argv_f[8] = argv_f[7] + 90  # y8>y9-100
                elif argv[7] == (argv[8] - 100):
                    return argv_f
                else:
                    argv_f[8] = argv_f[7] + 110
            else:
                if argv[7] > argv[8]:
                    argv_f[7] = argv_f[8] + 1
                elif argv[7] == argv[8]:  # 无解
                    return argv_f
                else:
                    argv_f[8] = argv_f[7] + 1
            argv_ff = argv_f.copy()
            if argv_f[3] <= argv_f[5]:
                if argv_f[6] == 0:
                    return argv_ff
                else:
                    argv_ff[6] = argv_f[6] - 1
            else:
                if argv_f[6] == 3:
                    return argv_ff
                else:
                    argv_ff[6] = argv_f[6] + 1
        return argv_ff

    def MR9(self,argv):
        o_s = TCAS().Tcas(argv)
        argv_f = argv.copy()
        argv_ff = argv_f.copy()
        if o_s == 'UPWARD_RA':
            if argv[6] == 3:
                return argv_ff
            else:
                argv_f[6] = argv[6] + 1
            argv_ff = argv_f.copy()
            argv_ff[8] = argv_f[8] - 10
        elif o_s == 'DOWNWARD_RA':
            if argv[6] == 0:
                return argv_ff
            else:
                argv_f[6] = argv[6] - 1
            argv_ff = argv_f.copy()
            argv_ff[7] = argv_f[7] + 10  # y8>x8
            if argv_f[11] == 1:
                argv_ff[8] = argv_ff[7] + 110  # y8+100<=y9
            else:
                argv_ff[8] = argv_ff[7] + 10  # y8<=y9
        elif o_s == 'UNRESOLVED':
            if argv[3] <= argv[5]:
                if argv[6] == 0:
                    return argv_ff
                else:
                    argv_f[6] = argv[6] - 1
            else:
                if argv[6] == 3:
                    return argv_ff
                else:
                    argv_f[6] = argv[6] + 1
            argv_ff = argv_f.copy()
            argv_ff[7] = argv_f[7] - 10  # y8<x8
            argv_ff[8] = argv_f[8] + 10  # y9>x9
            if argv_f[11] == 1:
                if argv_f[7] > (argv_f[8] - 100):  # x8>x9-100
                    argv_ff[8] = argv_ff[7] + 90  # y8>y9-100
                elif argv_f[7] == (argv_f[8] - 100):
                    return argv_ff
                else:
                    argv_ff[8] = argv_ff[7] + 110
            else:
                if argv_f[7] > argv_f[8]:
                    argv_ff[7] = argv_ff[8] + 1
                elif argv_f[7] == argv_f[8]:  # 无解
                    return argv_ff
                else:
                    argv_ff[8] = argv_ff[7] + 1
        return argv_ff
