'''

Row normalization function that normalizes each row of the matrix x

'''
# Row Normalization Function


def Row_Normalization_Function(x):
    """
    Normalizes each row of the matrix x (to have unit length)

    Argument:
    x -- A numpy matrix of shape (n, m)

    Returns:
    x -- The normalized (by row) numpy matrix. You are allowed to modify x.
    """

    # Compute x_norm as the norm 2 of x, 2norm is selected by picking ord = 2
    # axis is 1 for row-wise calculation
    x_norm = np.linalg.norm(x, ord=2, axis=1, keepdims=True)

    # Divide x by its norm
    x = x/x_norm

    return x
