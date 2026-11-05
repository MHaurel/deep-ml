def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	values, rows, columns = [], [], [0]
	n_rows = len(dense_matrix)
	n_cols = len(dense_matrix[0])

	for i in range(n_cols):
		n_0 = 0
		non_0_per_col = 0
		for j in range(n_rows):
			if dense_matrix[j][i] != 0:
				values.append(dense_matrix[j][i])
				rows.append(j)
				#columns.append(i)

				non_0_per_col += 1
			else:
				n_0 += 1

		if n_0 == n_rows:
			columns.append(0)
		else:
			columns.append(columns[-1]+non_0_per_col)

	#columns.append(len(values))

	return values, rows, columns
