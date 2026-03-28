import math

class Trisquare:
    def trisquare(self, argv):
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
            print('Not a triangle')
            return 0
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if pow(Max, 2) < pow(mid, 2) + pow(Min, 2):
            # 锐角三角形
            if Max == mid:
                # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))
                return Min * h / 2
            elif Min == mid:
                # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                return Max * h / 2
            else:
                # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) / 2
                return math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
        if pow(Max, 2) == pow(mid, 2) + pow(Min, 2):
            return mid * Min / 2
        if Min == mid:
            # 钝角等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            return Max * h / 2
        else:
            # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            return Max * h / 2

class Mutant1:
    def trisquare(self, argv):
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
            print('Not a triangle')
            return area
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if pow(Max, 2) < pow(mid, 2) + pow(Min, 2):  # 锐角三角形
            # print('Acute triangle')
            if Max == mid:  # 顶角小于或等于60度的等腰三角形  e.g. [5, 5, 4]
                h = math.sqrt(pow(Max, 2) - pow(mid / 2, 2))  # h = math.sqrt(pow(Max,2)-pow(Min/2,2))
                area = Min * h / 2
                return area
            elif Min == mid:  # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                area = Max * h / 2
                return area
            else:  # 不规则的锐角三角形, 海伦公式计算
                p = (Max + mid + Min) / 2
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area
        if (pow(Max, 2) == pow(mid, 2) + pow(Min, 2)):
            # print('Right-angled triangle') #直角三角形
            area = mid * Min / 2
            return area
        # print('Obtuse triangle')
        if (Min == mid):  # 等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h / 2
            return area
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            return area

class Mutant2:
    def trisquare(self, argv):
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if (a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b):
            print('Not a triangle')
            return area
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if (pow(Max, 2) < pow(mid, 2) + pow(Min, 2)):  # 锐角三角形
            # print('Acute triangle')
            if (Max == mid):  # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))
                area = Min * h / 2
                return area
            elif (Min == mid):  # 顶角大于60度的等腰三角形 [4, 4, 5]
                h = math.sqrt(pow(Min, 2) - pow(mid / 2, 2))  # h = math.sqrt(pow(Min,2)-pow(Max/2,2))
                area = Max * h / 2
                return area
            else:  # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) / 2
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area
        if (pow(Max, 2) == pow(mid, 2) + pow(Min, 2)):
            # print('Right-angled triangle') #直角三角形
            area = mid * Min / 2
            return area
        # print('Obtuse triangle')
        if (Min == mid):  # 等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h / 2
            return area
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            return area

class Mutant3:
    def trisquare(self, argv):
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if (a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b):
            print('Not a triangle')
            return area
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if (pow(Max, 2) < pow(mid, 2) + pow(Min, 2)):  # 锐角三角形
            # print('Acute triangle')
            if (Max == mid):  # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))
                area = Min * h / 2
                return area
            elif (Min == mid):  # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                area = Max * h / 2
                return area
            else:  # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) * 2  # p = (Max + mid + Min)/2
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area
        if (pow(Max, 2) == pow(mid, 2) + pow(Min, 2)):
            # print('Right-angled triangle') #直角三角形
            area = mid * Min / 2
            return area
        # print('Obtuse triangle')
        if (Min == mid):  # 等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h / 2
            return area
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            return area

class Mutant4:
    def trisquare(self, argv):
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if (a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b):
            print('Not a triangle')
            return area
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if (pow(Max, 2) < pow(mid, 2) + pow(Min, 2)):  # 锐角三角形
            # print('Acute triangle')
            if (Max == mid):  # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))
                area = Min * h / 2
                return area
            elif (Min == mid):  # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                area = Max * h / 2
                return area
            else:  # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) / 2
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area
        if (pow(Max, 2) == pow(mid, 2) + pow(Min, 2)):  # 直角三角形
            # print('Right-angled triangle')
            area = mid * Min  # mid*Min/2
            return area
        # print('Obtuse triangle')
        if (Min == mid):  # 钝角等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h / 2
            return area
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            return area

class Mutant5:
    def trisquare(self, argv):
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if (a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b):
            print('Not a triangle')
            return area
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if (pow(Max, 2) < pow(mid, 2) + pow(Min, 2)):  # 锐角三角形
            # print('Acute triangle')
            if (Max == mid):  # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))
                area = Min * h / 2
                return area
            elif (Min == mid):  # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                area = Max * h / 2
                return area
            else:  # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) / 2
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area
        if (pow(Max, 2) == pow(mid, 2) + pow(Min, 2)):
            # print('Right-angled triangle') #直角三角形
            area = mid * Min / 2
            return area
        # print('Obtuse triangle')
        if (Min == mid):  # 等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h  # Max*h/2
            return area
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            return area

class Mutant6:
    def trisquare(self, argv):
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if (a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b):
            print('Not a triangle')
            return area
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if (pow(Max, 2) < pow(mid, 2) + pow(Min, 2)):  # 锐角三角形
            # print('Acute triangle')
            if (Max == mid):  # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))
                area = Min * h / 2
                return area
            elif (Min == mid):  # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                area = Max * h / 2
                return area
            else:  # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) / 2
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area
        if (pow(Max, 2) == pow(mid, 2) + pow(Min, 2)):
            # print('Right-angled triangle') #直角三角形
            area = mid * Min / 2
            return area
        # print('Obtuse triangle')
        if (Min == mid):  # 等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h / 2
            return area
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(Min, 2) - pow(mid, 2)) / (2 * Max)  # x = (pow(Max,2)+pow(mid,2)-pow(Min,2))/(2*Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            return area

class TriFactory:
    def __init__(self, class_name):
        self.class_name = class_name

    def getTri(self):
        if self.class_name == "Mutant1":
            return Mutant1()
        elif self.class_name == "Mutant2":
            return Mutant2()
        elif self.class_name == "Mutant3":
            return Mutant3()
        elif self.class_name == "Mutant4":
            return Mutant4()
        elif self.class_name == "Mutant5":
            return Mutant5()
        elif self.class_name == "Mutant6":
            return Mutant6()
        else:
            return Trisquare()
