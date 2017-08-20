import numpy as np


def logistic_regression(x, y):
    """
    This computes logistic regression

    :param x: Input: shape should be (features x examples)
    :param y: Output: shape should be (1 * examples)
    :return: The learned parameters
    """
    dw = np.zeros(x.shape[0], x.shape[1])
    db = np.zeros(x.shape[0], x.shape[1])
    J = 0
