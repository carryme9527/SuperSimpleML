# -*- coding: UTF-8 -*-

import numpy as np


def shuffle(X, y):
    columns = X.size // len(X)
    arr = np.c_[X.reshape(len(X), -1), y.reshape(len(y), -1)]
    np.random.shuffle(arr)
    X_ = arr[:, :columns].reshape(X.shape)
    y_ = arr[:, columns:].reshape(y.shape)
    return X_, y_


def split(X, y, pcts=[0.8, 0.2]):
    size = X.shape[0]

    s = 0
    returns = []
    for pct in pcts:
        e = s + int(size * pct)
        returns.append(X[s:e])
        returns.append(y[s:e])
        s = e

    return tuple(returns)
