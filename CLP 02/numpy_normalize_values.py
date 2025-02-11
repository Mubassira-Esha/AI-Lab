import numpy as np

seed = int(input("Enter a random seed (any number): "))
np.random.seed(seed)
random_values = np.random.rand(100)
normalized_values = (random_values - np.min(random_values)) / (np.max(random_values) - np.min(random_values))

print("Normalized Values:\n", normalized_values)
