'''
Dot product implemented in python and numpy(inner product)

'''
import numpy as np
# Here we have two vectors x1, x2

x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

# Inner product of the two vectors in python


def Python_Inner_Product(a, b):
    # step 1: initialize our inner product
    inner_product = 0

    # step 2: run through everything in the first vector
    for i in range(len(a)):

        # get the scaler
        inner_product = inner_product + a[i] * b[i]

    return inner_product


# let's now write the same function in numpy, vectorized dot product
def Numpy_Inner_Product(a, b):
    inner_product = np.dot(a, b)
    return inner_product
