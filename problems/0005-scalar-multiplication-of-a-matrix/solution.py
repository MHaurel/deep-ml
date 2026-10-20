def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	matrix_c = matrix
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			matrix_c[i][j] = matrix[i][j] * scalar

	return matrix_c