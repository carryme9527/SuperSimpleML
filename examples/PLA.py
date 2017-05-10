# -*- coding: UTF-8 -*-

from SuperSimpleML.algorithm import PLA
from SuperSimpleML.datasets import generator
from SuperSimpleML.datasets import ds_utils
from SuperSimpleML.evaluation import calculateAccuracy


def main(dim=2, size=100):
    X, y = generator.genRandomLinearBinaryDataset(dim, size)
    X, y = ds_utils.shuffle(X, y)
    train_X, train_y, test_X, test_y = ds_utils.split(X, y, [0.8, 0.2])

    algorithm = PLA()
    algorithm.train(train_X, train_y)
    return calculateAccuracy(test_y, algorithm.test(test_X))


if __name__ == '__main__':
    dim = 4
    size = 200
    print main(dim, size)
