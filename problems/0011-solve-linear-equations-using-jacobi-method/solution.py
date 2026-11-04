import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros_like(b, dtype=float)

	for l in range(n):
		x_new = np.zeros_like(x)
		for k in range(len(A)):
			x_new[k] = (1/A[k][k]) * (b[k] - sum(A[k][j] * x[j] for j in range(len(A)) if j != k))

		x = x_new

	return x