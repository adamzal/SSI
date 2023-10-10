import matplotlib.pyplot as plt
import numpy as np

from SSI.lab1.lab1 import *


class Diagram:

    def __init__(self, n=1, m=1) -> None:
        self.fig, self.ax = plt.subplots(n, m)
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']
        self.markers = ['o', 's', '^', 'v', '<', '>', 'P', 'D', 'X', '*']

        self.seria = 0

    def clear_diagram(self) -> None:
        self.ax.clear()

    def plot_line_diagram(self, x, y) -> None:
        color = self.colors[self.seria % 10]
        self.ax.plot(x, y, color=color)
        self.seria += 1

    def plot_point_diagram(self, x, y) -> None:
        color = self.colors[self.seria % 10]
        marker = self.markers[self.seria % 10]
        self.ax.scatter(x, y, color=color, marker=marker)
        self.seria += 1

    def show_diagram(self) -> None:
        plt.show()


if __name__ == "__main__":
    dia_1 = Diagram()
    dia_1.plot_line_diagram(np.linspace(-1, 1, 100), -np.sin(np.linspace(-1, 1, 100) * 0.5 * np.pi + 0.5 * np.pi))
    dia_1.plot_point_diagram([-1, 0, 1], [1, 0, 1])
    dia_1.plot_line_diagram(np.append(np.linspace(-2, 2, 20), np.linspace(2, -2, 20)),
                            np.append(np.sqrt(4 - np.linspace(-2, 2, 20) ** 2),
                                      -np.sqrt(4 - np.linspace(-2, 2, 20) ** 2)))
    dia_1.show_diagram()

    ds_iris = DataSet("../lab1/iris.txt")
    iris_1 = ds_iris.file[ds_iris.file[4] == 1]
    iris_2 = ds_iris.file[ds_iris.file[4] == 2]
    iris_3 = ds_iris.file[ds_iris.file[4] == 3]

    dia_2 = Diagram()
    dia_2.plot_point_diagram(iris_1[2], iris_1[3])
    dia_2.plot_point_diagram(iris_2[2], iris_2[3])
    dia_2.plot_point_diagram(iris_3[2], iris_3[3])
    dia_2.show_diagram()

    dia_3 = Diagram()
    dia_3.plot_point_diagram(iris_1[1], iris_1[3])
    dia_3.plot_point_diagram(iris_2[1], iris_2[3])
    dia_3.plot_point_diagram(iris_3[1], iris_3[3])
    dia_3.show_diagram()

    dia_4 = Diagram()
    dia_4.plot_point_diagram(iris_1[0], iris_1[3])
    dia_4.plot_point_diagram(iris_2[0], iris_2[3])
    dia_4.plot_point_diagram(iris_3[0], iris_3[3])
    dia_4.show_diagram()

    dia_5 = Diagram()
    dia_5.plot_point_diagram(iris_1[1], iris_1[2])
    dia_5.plot_point_diagram(iris_2[1], iris_2[2])
    dia_5.plot_point_diagram(iris_3[1], iris_3[2])
    dia_5.show_diagram()
