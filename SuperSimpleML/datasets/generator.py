# -*- coding: UTF-8 -*-

import numpy as np


def genRandomLinearBinaryDataset(dim=2, size=100):
    lower_pct = 0.2
    upper_pct = 0.8

    def linear(W, x):
        product = np.inner(W, x)
        if product > 0:
            return 1
        elif product <= 0:
            return -1

    def get_data():
        W = np.random.rand(dim + 1) - 0.5
        X = []
        y = []

        for i in range(size):
            x = np.random.rand(dim + 1) - 0.5
            x[-1] = 1

            X.append(x[:-1])
            y.append(linear(W, x))
        return np.array(X), np.array(y)

    X, y = get_data()
    while not int(size * lower_pct) < y[y == 1].shape[0] < int(
            size * upper_pct):
        X, y = get_data()
    return X, y
