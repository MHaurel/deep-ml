import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	"""
	vectors: list of list, list i holds the N observations of feature i (all feature have same N)
	"""
	X = np.array(vectors)

	def cov(i, j):
		# tested: pass
		n = len(i)

		mean_i, mean_j = np.mean(np.array(i)), np.mean(np.array(j))

		return (1 / (n-1)) * sum([(xi-mean_i)*(xj-mean_j) for xi, xj in zip(i, j)])

	#cov_factor = cov(X[0], X[1])
	
	cov_matrix = np.array([
		[cov(X[i], X[j]) for j in range(X.shape[0])]
		for i in range(X.shape[0])
	])


	return cov_matrix