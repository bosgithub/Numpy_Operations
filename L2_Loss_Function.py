'''
L2 Loss Function

L2 loss or least square error function implemented in numpy

'''


def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)

    Returns:
    loss -- the value of the L2 loss function defined above
    """
    # find the difference between predicted and true label
    # square it, then sum this at every data point
    loss = np.sum((yhat - y)**2)

    return loss
