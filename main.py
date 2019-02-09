
import random
import numpy as np
import matplotlib.pyplot as plt


def left_right_stay(size=100, center=0, weights=(1, 1, 1)):
	weight_array = [-1] * weights[0] + \
		              [0] * weights[1] + \
		              [1] * weights[2]

	distribution = []

	for i in range(size):
		position = center

		while True:
			choice = random.choice(weight_array)

			position += choice

			if choice == 0:
				distribution.append(position)
				break

	return distribution


def pairing(arr):
	uniques, counts = np.unique(arr, return_counts=True)
	return list(zip(uniques, counts))


def main():
	dist = left_right_stay(size=1000000)
	pairs = pairing(dist)

	x, y = list(zip(*pairs))
	plt.plot(x, y, 'kx')
	plt.show()


if __name__ == '__main__':
	main()
