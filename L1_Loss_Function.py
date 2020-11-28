'''
L1 Loss Function

L1 loss or least absolute deviation function implemented in numpy

'''


def L1(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)

    Returns:
    loss -- the value of the L1 loss function defined above
    """

    # start with the absolute difference between predicted and
    # true value label, then sum the difference at every data points
    loss = np.sum(np.abs(yhat - y))

    return loss
