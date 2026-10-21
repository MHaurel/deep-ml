import numpy as np
def precision(y_true, y_pred):
	# Your code here
	tp = 0
	fp = 0

	for x_t, x_p in zip(y_true, y_pred):
		if x_p == 1:
			if x_t == 1:
				tp += 1
			else: # x_t = 0
				fp += 1

	if tp == 0 and fp == 0:
		return 0
	return tp / (tp+fp)