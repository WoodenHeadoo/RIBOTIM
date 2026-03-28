from decimal import Decimal

def duplicateMatrix(original_matrix):
    dup_matrix = []
    for row in range(len(original_matrix)):
        temp = []
        for col in range(len(original_matrix[0])):
            temp.append(original_matrix[row][col])
        dup_matrix.append(temp)
    return dup_matrix

def shuffleAttribute(original_matrix, shuffle_map):
    shuffled_matrix = duplicateMatrix(original_matrix)
    for row in range(len(shuffled_matrix)):
        for col in range(len(shuffled_matrix[0]) - 1):  # the last column, label info, is removed
            dict_value = shuffle_map[col]
            if not col == dict_value:
                shuffled_matrix[row][col] = original_matrix[row][dict_value]
    return shuffled_matrix

def getShuffleMap(training_set):
    origin_index = list(range(len(training_set[0]) - 1))  # the last column, label info, is removed
    # random.seed(k)
    #shuffle_index = random.sample(origin_index, len(origin_index))
    shuffle_index = [1, 3, 2, 0]
    shuffle_map = dict(zip(origin_index, shuffle_index))
    return shuffle_map

class MRs:
    def MR1(self, training_set, testing_set):
        k = Decimal(1)
        b = Decimal(5)
        ftc_train = duplicateMatrix(training_set)
        ftc_test = duplicateMatrix(testing_set)
        for row in range(len(training_set)):
            for col in range(len(training_set[0]) - 1):
                ftc_train[row][col] = k * Decimal(training_set[row][col]) + b
        for row in range(len(testing_set)):
            for col in range(len(testing_set[0]) - 1):
                ftc_test[row][col] = k * Decimal(testing_set[row][col]) + b
        return ftc_train, ftc_test

    def MR2(self, training_set, testing_set):
        shuffle_map = getShuffleMap(training_set)
        ftc_train = shuffleAttribute(training_set, shuffle_map)
        ftc_test = shuffleAttribute(testing_set, shuffle_map)
        return ftc_train, ftc_test

    def MR3(self, training_set, testing_set):
        k = Decimal(-1)
        b = Decimal(7)
        ftc_train = duplicateMatrix(training_set)
        ftc_test = duplicateMatrix(testing_set)
        for row in range(len(training_set)):
            for col in range(len(training_set[0]) - 1):
                ftc_train[row][col] = k * Decimal(training_set[row][col]) + b
        for row in range(len(testing_set)):
            for col in range(len(testing_set[0]) - 1):
                ftc_test[row][col] = k * Decimal(testing_set[row][col]) + b

        shuffle_map = getShuffleMap(ftc_train)
        fftc_train = shuffleAttribute(ftc_train, shuffle_map)
        fftc_test = shuffleAttribute(ftc_test, shuffle_map)
        return fftc_train, fftc_test

    def MR4(self, training_set, testing_set):
        shuffle_map = getShuffleMap(training_set)
        ftc_train = shuffleAttribute(training_set, shuffle_map)
        ftc_test = shuffleAttribute(testing_set, shuffle_map)

        k = Decimal(2)
        b = Decimal(-15)
        fftc_train = duplicateMatrix(ftc_train)
        fftc_test = duplicateMatrix(ftc_test)
        for row in range(len(training_set)):
            for col in range(len(training_set[0]) - 1):
                fftc_train[row][col] = k * Decimal(ftc_train[row][col]) + b
        for row in range(len(testing_set)):
            for col in range(len(testing_set[0]) - 1):
                fftc_test[row][col] = k * Decimal(ftc_test[row][col]) + b
        return fftc_train, fftc_test
