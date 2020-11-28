'''
Outer product

given two vectors x1 and x2, the outer product yields a matrix that
for each element in x1, is multiplied by each element in x2

example: x1 is cost of spending in different categories such as food, cloth
x2 is tax on city, province, countries, outer product gives the portion of
the tax on the category(food) on the specific regional level

'''

# Here we have two vectors x1, x2

x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

# Python method with for loops


def Python_Outer_Product(a, b):

    # Initialize an empty matrix with only zeros
    outer = np.zeros((len(a), len(b)))
    # For each value in the first vector
    for i in range(len(a)):
        # We multiply by everythin in the second vector
        for j in range(len(b)):
            # populate the empty matrix
            outer[i, j] = a[i]*b[j]

    return outer


# Numpy method
def Numpy_Outer_Product(a, b):
    outer = np.outer(x1, x2)
    return outer
