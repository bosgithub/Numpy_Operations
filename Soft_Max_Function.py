'''
    Softmax Max Function

    A logistic function to multiple dimensions. It is used in multinomial logistic regression 
    used as the last activation function of a neural network to normalize the output of a 
    network to a probability distribution over predicted output classes
'''


#   Softmax Max Function:

def softmax(x):
    """Calculates the softmax for matrices of shape (m,n)

    Argument:
    x -- A numpy matrix of shape (m,n)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (m,n)
    """

    # get the exponent term in the numerator first
    x_exp = np.exp(x)

    # Create a vector x_sum that sums each row of x_exp
    x_sum = np.sum(x_exp, axis=1, keepdims=True)

    # Compute softmax(x) by dividing x_exp by x_sum
    s = x_exp/x_sum

    return s
