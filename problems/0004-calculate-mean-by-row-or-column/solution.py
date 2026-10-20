def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == 'row':
		for i in range(len(matrix)):
			row_mean = []
			for j in range(len(matrix[i])):
				row_mean.append(matrix[i][j])
			means.append(sum(row_mean)/len(row_mean))
	else:
		n_row = len(matrix)
		n_col = len(matrix[0])
		for j in range(n_col):
			# j: second counter
			col_mean = []
			for i in range(n_row):
				# i: first counter
				col_mean.append(matrix[i][j])
			means.append(sum(col_mean)/len(col_mean))

			
#				col_mean.append(matrix[0][0])
#				col_mean.append(matrix[1][0])
#				col_mean.append(matrix[2][0])
#
#				col_mean.append(matrix[0][1])
#				col_mean.append(matrix[1][1])
#				col_mean.append(matrix[2][1])
#
#				col_mean.append(matrix[0][2])
#				col_mean.append(matrix[1][2])
#				col_mean.append(matrix[2][2])

	return means