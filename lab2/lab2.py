import matplotlib.pyplot as plt
import numpy as np

from SSI.lab1.lab1 import *


class Diagram:

    def __init__(self, n: int = 1, m: int = 1) -> None:
        self.fig, self.ax = plt.subplots(n, m)
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']
        self.markers = ['o', 's', '^', 'v', '<', '>', 'P', 'D', 'X', '*']

        self.seria = 0

    def clear_diagram(self) -> None:
        self.ax.clear()

    def plot_line_diagram(self, x: list | np.ndarray, y: list | np.ndarray, label: str) -> None:
        color = self.colors[self.seria % 10]
        self.ax.plot(x, y, color=color, label=label)
        self.seria += 1

    def plot_point_diagram(self, x: list | np.ndarray, y: list | np.ndarray, label: str) -> None:
        color = self.colors[self.seria % 10]
        marker = self.markers[self.seria % 10]
        self.ax.scatter(x, y, color=color, marker=marker, label=label)
        self.seria += 1

    @staticmethod
    def set_labels(x_label: str, y_label: str) -> None:
        plt.xlabel(x_label)
        plt.ylabel(y_label)

    @staticmethod
    def set_title(title: str) -> None:
        plt.title(title)

    def set_legend(self, legend: str | list) -> None:
        self.ax.legend(legend)

    def show_diagram(self) -> None:
        self.ax.legend()
        plt.show()


if __name__ == "__main__":
    dia_1 = Diagram()
    dia_1.plot_line_diagram(np.linspace(-1, 1, 100), -np.sin(np.linspace(-1, 1, 100) * 0.5 * np.pi + 0.5 * np.pi),
                            "usmiech")
    dia_1.plot_point_diagram([-1, 0, 1], [1, 0, 1], 'oczy i nos')
    dia_1.plot_line_diagram(np.append(np.linspace(-2, 2, 20), np.linspace(2, -2, 20)),
                            np.append(np.sqrt(4 - np.linspace(-2, 2, 20) ** 2),
                                      -np.sqrt(4 - np.linspace(-2, 2, 20) ** 2)), "obrys twarzy")
    dia_1.set_labels("Oś X", "Oś y")
    dia_1.show_diagram()

    ds_iris = DataSet("../lab1/iris.txt")
    ds_atr = DataSet("../lab1/iris-type.txt")

    text = ds_atr.get_value(0, ds_atr.file.shape[0] - 1)
    text = text.replace("class(", "").rstrip(")")
    pairs = text.split(",")

    result_dict = {}
    for pair in pairs:
        num, name = pair.split("=")
        result_dict[int(num)] = name

    iris_1 = ds_iris.file[ds_iris.file[4] == 1]
    iris_2 = ds_iris.file[ds_iris.file[4] == 2]
    iris_3 = ds_iris.file[ds_iris.file[4] == 3]

    dia_2 = Diagram()
    dia_2.plot_point_diagram(iris_1[2], iris_1[3], f"{result_dict[1]}")
    dia_2.plot_point_diagram(iris_2[2], iris_2[3], f"{result_dict[2]}")
    dia_2.plot_point_diagram(iris_3[2], iris_3[3], f"{result_dict[3]}")
    dia_2.set_labels(f"{ds_atr.get_value(0, 2)}", f"{ds_atr.get_value(0, 3)}")
    dia_2.show_diagram()

    dia_3 = Diagram()
    dia_3.plot_point_diagram(iris_1[1], iris_1[3], f"{result_dict[1]}")
    dia_3.plot_point_diagram(iris_2[1], iris_2[3], f"{result_dict[2]}")
    dia_3.plot_point_diagram(iris_3[1], iris_3[3], f"{result_dict[3]}")
    dia_2.set_labels(f"{ds_atr.get_value(0, 1)}", f"{ds_atr.get_value(0, 3)}")
    dia_3.show_diagram()

    dia_4 = Diagram()
    dia_4.plot_point_diagram(iris_1[0], iris_1[3], f"{result_dict[1]}")
    dia_4.plot_point_diagram(iris_2[0], iris_2[3], f"{result_dict[2]}")
    dia_4.plot_point_diagram(iris_3[0], iris_3[3], f"{result_dict[3]}")
    dia_2.set_labels(f"{ds_atr.get_value(0, 0)}", f"{ds_atr.get_value(0, 3)}")
    dia_4.show_diagram()

    dia_5 = Diagram()
    dia_5.plot_point_diagram(iris_1[1], iris_1[2], f"{result_dict[1]}")
    dia_5.plot_point_diagram(iris_2[1], iris_2[2], f"{result_dict[2]}")
    dia_5.plot_point_diagram(iris_3[1], iris_3[2], f"{result_dict[3]}")
    dia_2.set_labels(f"{ds_atr.get_value(0, 1)}", f"{ds_atr.get_value(0, 2)}")
    dia_5.show_diagram()
