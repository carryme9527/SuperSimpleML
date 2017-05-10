# -*- coding: UTF-8 -*-

from PLA import PLA
import numpy as np
from ..evaluation import calculateAccuracy


class PocketPLA():
    def __init__(self):
        pass

    def test(self, X):
        X_ = np.append(X, np.ones((X.shape[0], 1)), axis=1)
        y_ = np.sign(np.inner(self.W, X_))
        return y_

    def train(self, X, y, T=5):
        dim = X.shape[1]
        best_W = np.zeros(dim + 1)
        best_accuracy = 0

        self.W = best_W
        for t in range(T):
            for i in range(X.shape[0]):
                x = np.append(X[i], [1])
                y_ = np.sign(np.inner(self.W, x))
                if y_ != y[i]:
                    self.W = self.W + y[i] * x

            accuracy = calculateAccuracy(y, self.test(X))
            if accuracy > best_accuracy:
                best_accuracy, best_W = accuracy, self.W

        self.W = best_W
