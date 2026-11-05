import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	values, columns, rows = [], [], []

	size = len(dense_matrix)
	cum_row = 0
	rows.append(cum_row)
	for i in range(size):
		n_row = 0
		for j in range(size):
			if dense_matrix[i][j] != 0:
				values.append(dense_matrix[i][j])
				columns.append(j)
				n_row += 1

		cum_row+=n_row
		rows.append(cum_row)

	return values, columns, rows
