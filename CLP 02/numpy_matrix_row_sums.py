import numpy as np

# Taking user input for the range of random numbers
low = int(input("Enter the lower bound of random numbers: "))
high = int(input("Enter the upper bound of random numbers: "))

# Generating a 5x5 matrix with random integers in the given range
matrix = np.random.randint(low, high, (5, 5))

# Computing row-wise sums
row_sums = matrix.sum(axis=1)

# Displaying the matrix and row-wise sums
print("\nGenerated 5x5 Random Matrix:\n", matrix)
print("\nRow-wise Sums:", row_sums)
