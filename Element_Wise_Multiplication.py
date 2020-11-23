'''
Element-wise multiplication

'''
import numpy as np
# Here we have two vectors x1, x2

x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]


#  Element wise multiplication of the two vectors in python

def Python_Element_Wise_Multiplication(a, b):
    # Initialize
    new_vector = []

    # Run loop to append
    for i in range(len(a)):
        new_vector.append(a[i] * b[i])

    return new_vector


def Python_Element_Wise_Multiplication(a, b):
    # Initialize
    new_vector = np.zeros(len(a))

    # Run loop for assignment
    for i in range(len(a)):
        new_vector[i] = a[i] * b[i]

    return new_vector


# let's now write the same function in numpy

def Numpy_Element_Wise_Multiplication(a, b):
    multiplication = np.multiply(x1, x2)
    return multiplication
