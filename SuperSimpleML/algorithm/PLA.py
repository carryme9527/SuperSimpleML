# -*- coding: UTF-8 -*-

import numpy as np


class PLA():
    def __init__(self, dim):
        self.dim = dim
        self.W = np.zeros(self.dim + 1)
        self.X = np.zeros((0, dim))
        self.y = np.array([])
        self.T = 0

    def test(self, X):
        X_ = np.append(X, np.ones((X.shape[0], 1)), axis=1)
        y_ = np.inner(self.W, X_)
        y_[y_ > 0] = 1
        y_[y_ <= 0] = -1
        return y_

    def _append_training_data(self, X, y):
        self.X = np.append(self.X, X, axis=0)
        self.y = np.append(self.y, y, axis=0)

    def train(self, X, y):
        self._append_training_data(X, y)
        while True:
            self.T += 1
            for i in range(self.X.shape[0]):
                x = np.append(self.X[i], [1])
                y_ = 1 if np.inner(self.W, x) > 0 else -1
                if y_ != self.y[i]:
                    self.W = self.W + self.y[i] * x
                    break
            else:
                return
