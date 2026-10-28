import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	def mse(probabilities, labels):
		return sum([(x-y)**2 for x,y in zip(probabilities, labels)]) / len(probabilities)

	def sigmoid(z):
		return 1 / (1+math.exp(-z))

	probabilities = []
	for feature in features:
		z = sum([x*y for x, y in zip(feature, weights)]) + bias
		z_act = sigmoid(z)
		probabilities.append(round(z_act, 4))

	mse_value = mse(probabilities, labels)

	return probabilities, mse_value