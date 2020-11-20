'''

Reshaping function:

takes an input of shape (length, height, 3) then returns a vector of shape (length*height*3, 1)

'''

# Reshaping_Function:


def Reshaping_Function(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)

    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """

    v = image.reshape((image.shape[0]*image.shape[1]*image.shape[2], 1))

    return v
