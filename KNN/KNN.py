import math
import operator
from decimal import Decimal

class KNN:

    def __init__(self):
        # Configuration
        self.trainingSet = []
        self.testSet = []
        self.accuracy = 0
        self.k = 3
        self.default_label = "Iris-setosa"

    def setDefaultLabelabel(self, default_label):
        self.default_label = default_label

    def printInfo(self):
        print('Accuracy: ' + repr(self.accuracy) + '%')

    def setInput(self, trainingSet, testSet):
        self.trainingSet = trainingSet
        self.testSet = testSet

    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            try:
                distance += pow((Decimal(instance1[x]) - Decimal(instance2[x])), 2)
            except TypeError as t:
                print(t)
        return math.sqrt(Decimal(distance))

    def getNeighbors(self, testInstance):
        distances = []
        length = len(testInstance) - 1
        for x in range(len(self.trainingSet)):
            dist = self.euclideanDistance(testInstance, self.trainingSet[x], length)
            distances.append((self.trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(self.k):
            neighbors.append(distances[x][0])
        return neighbors

    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        if sortedVotes[0][1] == 1:
            return self.default_label
        else:
            return sortedVotes[0][0]

    def getPredications(self):
        predictions = []
        for x in range(len(self.testSet)):
            neighbors = self.getNeighbors(self.testSet[x])
            result = self.getResponse(neighbors)
            predictions.append(result)
        return predictions


class MU_1_KNN(KNN):

    def __init__(self):
        super(MU_1_KNN, self).__init__()

    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((Decimal(instance1[x]) + Decimal(instance2[x])), 2)  # - ---> +
        return math.sqrt(distance)


class MU_2_KNN(KNN):
    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance = pow((Decimal(instance1[x]) - Decimal(instance2[x])), 2)  # += ---> =
        return math.sqrt(distance)


class MU_3_KNN(KNN):
    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((Decimal(instance1[x]) - Decimal(instance2[x])), 2)
        return distance  # remove math.sqrt


class MU_4_KNN(KNN):

    def __init__(self):
        super(MU_4_KNN, self).__init__()

    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((Decimal(instance1[x]) / Decimal(instance2[x])), 2)  # - ---> /
        return math.sqrt(distance)


class MU_5_KNN(KNN):
    def getNeighbors(self, testInstance):
        distances = []
        length = len(testInstance) - 1
        for x in range(len(self.trainingSet)):
            dist = self.euclideanDistance(testInstance, self.trainingSet[x], length)
            distances.append((self.trainingSet[x], dist))
        # distances.sort(key=operator.itemgetter(1))              # remove this line
        neighbors = []
        for x in range(self.k):
            neighbors.append(distances[x][0])
        return neighbors


class MU_6_KNN(KNN):
    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors) - 1):  # len(neighbors)
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]


class MU_7_KNN(KNN):
    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] *= 1  # + --> *
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]


class MU_8_KNN(KNN):
    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] = 1  # += ---> =
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]


class MU_9_KNN(KNN):
    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=False)  # True --> False
        if sortedVotes[0][1] == 1:
            return self.default_label
        else:
            return sortedVotes[0][0]

class MU_10_KNN(KNN):
    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            try:
                distance *= pow((Decimal(instance1[x]) - Decimal(instance2[x])), 2)  # += ----> *=
            except TypeError as t:
                print(t)
        return math.sqrt(distance)

class KNNFactory:
    def __init__(self, class_name):
        self.class_name = class_name

    def getKNN(self):
        if (self.class_name == "MU_1_KNN"):
            return MU_1_KNN()
        elif (self.class_name == "MU_2_KNN"):
            return MU_2_KNN()
        elif (self.class_name == "MU_3_KNN"):
            return MU_3_KNN()
        elif (self.class_name == "MU_4_KNN"):
            return MU_4_KNN()
        elif (self.class_name == "MU_5_KNN"):
            return MU_5_KNN()
        elif (self.class_name == "MU_6_KNN"):
            return MU_6_KNN()
        elif (self.class_name == "MU_7_KNN"):
            return MU_7_KNN()
        elif (self.class_name == "MU_8_KNN"):
            return MU_8_KNN()
        elif (self.class_name == "MU_9_KNN"):
            return MU_9_KNN()
        elif (self.class_name == "MU_10_KNN"):
            return MU_10_KNN()
        else:
            return KNN()
