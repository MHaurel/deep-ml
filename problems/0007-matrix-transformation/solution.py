import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	# check invertibility
	if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
		return -1

	inverse_T = np.linalg.inv(T)
	transformed_matrix = inverse_T @ A @ S
	return transformed_matrix