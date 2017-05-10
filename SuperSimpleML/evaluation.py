# -*- coding: UTF-8 -*-

import numpy as np


def calculateAccuracy(y, y_):
    return np.average(y == y_)
