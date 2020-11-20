'''

let's build the sigmoid function

'''


# Sigmoid Function


# using function from math lib
import numpy as np
import math


def sigmoid_math(x):
    """
    Compute sigmoid of x using math

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """

    s = 1/(1+math.exp(-x))

    return s


# using function from numpy lib


def sigmoid_numpy(x):
    """
    Compute the sigmoid of x using numpy

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """

    s = 1/(1+np.exp(-x))

    return s
