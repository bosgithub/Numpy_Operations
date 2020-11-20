'''

Gradient of the sigmoid function

'''

# Derivative of sigmoid function


def sigmoid_derivative(x):
    """
    Compute the gradient of the sigmoid function with respect to its input x

    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    # Sigmoid function
    s = 1/(1+np.exp(-x))

    # Derivative of sigmoid function
    ds = s*(1-s)

    return ds
