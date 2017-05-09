# -*- coding: UTF-8 -*-


def calculateAccuracy(y, y_):
    correct = 0
    for i in range(len(y)):
        if y_[i] == y[i]:
            correct += 1
    accuracy = 100 * float(correct) / len(y)
    return accuracy
