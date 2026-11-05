import numpy as np

def make_diagonal(x):
	# Your code here
	size = len(x)
	diag_x = np.zeros((size, size), dtype=float)

	for i in range(size):
		for j in range(size):
			if i==j: diag_x[i][j] = x[i]

	return diag_x