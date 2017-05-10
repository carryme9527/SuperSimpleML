# -*- coding: UTF-8 -*-

import numpy as np


class PLA():
    def __init__(self):
        pass

    def test(self, X):
        X_ = np.append(X, np.ones((X.shape[0], 1)), axis=1)
        y_ = np.sign(np.inner(self.W, X_))
        return y_

    def train(self, X, y):
        dim = X.shape[1]
        self.W = np.zeros(dim + 1)
        while True:
            for i in range(X.shape[0]):
                x = np.append(X[i], [1])
                y_ = np.sign(np.inner(self.W, x))
                if y_ != y[i]:
                    self.W = self.W + y[i] * x
                    break
            else:
                return
