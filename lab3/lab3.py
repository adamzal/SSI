import random

from SSI.lab2.lab2 import *


class StrConv:

    def __init__(self, data: DataSet) -> None:
        self.data = data

    def convert_str_to_numbers(self, atr_num: list | np.ndarray) -> list | np.ndarray:
        res = []
        for el in range(self.data.file.shape[0]):
            tab = []
            for _ in atr_num:
                tab += [float(self.data.file.loc[el][_])]
            res += [tab]
        return res


class KMeans:

    def __init__(self, data: list, m: int = 4, n_iter: int = 100) -> None:
        self.data = data
        self.m = m
        self.n_iter = n_iter
        self.V = []

    @staticmethod
    def euklides_norm(x0, x1, y0, y1) -> np.core.numeric:
        return np.sqrt((float(x0) - float(x1)) ** 2 + (float(y0) - float(y1)) ** 2)

    def fit(self):
        self.V = random.sample(self.data, self.m)

        for _ in range(self.n_iter):
            groups = [[] for _ in range(self.m)]

            for s in range(len(self.data)):
                dist = [self.euklides_norm(self.data[s][0], v[0], self.data[s][1], v[1]) for v in self.V]
                us = np.argmin(dist)
                groups[us].append(self.data[s])

            new_V = []

            for j in groups:
                if j:
                    x = []
                    y = []
                    for i in range(len(j)):
                        x.append(j[i][0])
                        y.append(j[i][1])
                    new_V.append([np.mean(x), np.mean(y)])

            self.V = new_V

            if _ == 99:
                diag = Diagram()
                V_x = []
                V_y = []
                n = 1
                for j in groups:
                    if j:
                        x = []
                        y = []
                        for i in range(len(j)):
                            x.append(j[i][0])
                            y.append(j[i][1])
                    diag.plot_point_diagram(x, y, f"Grupa {n}")
                    n += 1

                for i in self.V:
                    V_x.append(i[0])
                    V_y.append(i[1])
                diag.plot_point_diagram(V_x, V_y, "Środki grup")
                diag.set_labels("Oś X", "Oś y")
                diag.set_title("Algorytm KMeans")
                diag.show_diagram()


if __name__ == "__main__":
    spirala = DataSet("spirala.txt", sep="   ")

    sc = StrConv(spirala)
    conv_data = sc.convert_str_to_numbers([0, 1])

    km = KMeans(conv_data, m=4)
    km.fit()
