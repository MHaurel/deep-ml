import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	inverse_C = np.linalg.inv(C)
	
	P = inverse_C @ B
	return P