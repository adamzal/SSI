import matplotlib.pyplot as plt
import numpy as np


class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def learn_pattern(self, pattern):
        pattern = np.array(pattern).flatten()
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    self.weights[i, j] += (2 * pattern[i] - 1) * (2 * pattern[j] - 1) / self.size

    def recall_pattern(self, pattern, max_iter=10):
        pattern = np.array(pattern).flatten()
        for _ in range(max_iter):
            for i in range(self.size):
                s = sum(self.weights[i, j] * pattern[j] for j in range(self.size) if j != i)
                pattern[i] = 1 if s >= 0 else -1
        return pattern


def read_data(file_name):
    with open(file_name, "r") as file:
        data = file.read().split("\n\n")

    main_tab = []
    for matrix in data:
        tab = np.array([list(map(int, row.split())) for row in matrix.strip().split('\n')]).flatten()
        main_tab.append(tab)

    return main_tab


if __name__ == "__main__":
    patterns = read_data("patterns.txt")
    test = read_data("test.txt")

    pattern_size = len(patterns[0])
    network = HopfieldNetwork(pattern_size)

    for i in range(len(test)):

        fig, ax = plt.subplots(1, 3)
        if i < len(patterns):
            network.learn_pattern(patterns[i])
            result = network.recall_pattern(test[i])
            ax[0].imshow(patterns[i].reshape((5, 5)), cmap='gray_r')
            ax[0].set_title("Pattern")
            ax[1].imshow(test[i].reshape((5, 5)), cmap='gray_r')
            ax[1].set_title("Test pattern before")
        else:
            network.learn_pattern(patterns[0])
            result = network.recall_pattern(test[i])
            ax[0].imshow(patterns[0].reshape((5, 5)), cmap='gray_r')
            ax[0].set_title("Pattern")
            ax[1].imshow(test[i].reshape((5, 5)), cmap='gray_r')
            ax[1].set_title("Test pattern before")

        ax[2].imshow(result.reshape((5, 5)), cmap='gray_r')
        ax[2].set_title("Test pattern after")
        plt.show()
