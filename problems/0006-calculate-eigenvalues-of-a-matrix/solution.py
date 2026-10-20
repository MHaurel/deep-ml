import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

	"""
	A 2x2 matrix can be represented as A=

	(a  b)
	(c  d)

	eigenvalues of this matrix A can be determined by solving the equation:

	det(A - (lambda*I)) = 0

	which simplified to a quadratic equation:

	lambda**2 - (tr(A) * lambda) + det(A) = 0

	tr(A) = a+d ; det(A) = ad - bc

	eigenvalues are : lambda
	"""
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]

	tr = a+d
	det = a*d - b*c

	# TODO: quadratic formula here to retrieve a, b, c
	aq = 1
	bq = -tr
	cq = det

	#print(aq, bq, cq)

	lambda_plus = (-bq + np.sqrt(bq**2 - (4 * aq * cq))) / (2 * aq)
	lambda_minus = (-bq - np.sqrt(bq**2 - (4 * aq * cq))) / (2 * aq)

	eigenvalues = [lambda_plus, lambda_minus]

	return eigenvalues