# -*- coding: UTF-8 -*-

import numpy as np
from datetime import datetime
from SuperSimpleML.algorithm import PLA
from SuperSimpleML.datasets import generator
from SuperSimpleML.datasets import ds_utils
from SuperSimpleML.evaluation import calculateAccuracy

def compare(dim=2, size=100):
    X, y = generator.genRandomLinearBinaryDataset(dim, size)
    print np.var(X, axis=0)
    print np.std(X, axis=0)
    X, y = ds_utils.shuffle(X, y)
    train_X, train_y, test_X, test_y = ds_utils.split(X, y, [0.8, 0.2])

    for normalized in [False, True]:
        ts = datetime.now()
        algorithm = PLA(dim, normalized)
        algorithm.train(train_X, train_y)
        accuracy = calculateAccuracy(test_y, algorithm.test(test_X))
        if normalized:
            print '    normalized', dim, size, accuracy, datetime.now() - ts
        else:
            print 'not normalized', dim, size, accuracy, datetime.now() - ts

if __name__ == '__main__':
    for dim in [2, 3, 4]:
        for size in [100, 200, 300]:
            compare(dim, size)
