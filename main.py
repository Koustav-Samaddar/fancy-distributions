
import time
import random
import numpy as np
import matplotlib.pyplot as plt

from itertools import chain
from scipy.stats import norm
from multiprocessing import Pool


def let_the_man_walk(center, weight_array, num):
	distribution = []

	for i in range(num):
		position = center

		while True:
			choice = random.choice(weight_array)
			position += choice

			if choice == 0:
				distribution.append(position)
				break

	return distribution


def left_right_stay(size=100, center=0, weights=(1, 1, 1)):
	num_threads = 4

	if len(weights) == 3:
		left_weight, center_weight, right_weight = weights
	elif len(weights) == 2:
		left_weight, center_weight = weights
		right_weight = left_weight
	else:
		raise ValueError('Argument `weights` must be a tuple of length 2 or 3')

	weight_array = [-1] * left_weight + \
		              [0] * center_weight + \
		              [1] * right_weight

	thread_distribution = [int(size / num_threads)] * (num_threads - 1)
	thread_distribution.append(size - sum(thread_distribution))

	param_distribution = map(lambda x: (center, weight_array, x), thread_distribution)

	with Pool(processes=4) as pool:
		distribution = pool.starmap(let_the_man_walk, param_distribution)

	return list(chain(*distribution))


def pairing(arr):
	uniques, counts = np.unique(arr, return_counts=True)
	return list(zip(uniques, counts))


def main():
	start = time.time()
	size = 10000000
	dist = left_right_stay(size=size, weights=(1, 1, 1))
	pairs = pairing(dist)

	x, y = zip(*pairs)
	y = [ i / size for i in y ]

	mean = np.mean(dist)
	var = np.var(dist)
	std = np.std(dist)
	end = time.time()

	print()
	print("Stats")
	print("Average: {0:.2f}".format(mean))
	print("Variance: {0:.2f}".format(var))
	print("Standard Deviation: {0:.2f}".format(std))

	print()
	print("Performance")
	print("Elapsed Time: {0:.2f}s".format(end - start))

	x_axis = np.arange(-100, 100, 0.001)
	plt.plot(x, y, 'rx')
	plt.plot(x_axis, norm.pdf(x_axis, mean, std), 'b-')

	plt.xlim((-100, 100))
	plt.show()


if __name__ == '__main__':
	main()
