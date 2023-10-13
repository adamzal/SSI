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


class FuzzyCMeans:
    def __init__(self, m, X, n_iter=100, fcm_m=2, epsilon=1e-10):
        self.m = m
        self.n_iter = n_iter
        self.epsilon = epsilon
        self.fcm_m = fcm_m
        self.X = np.array(X)
        self.M, self.n = self.X.shape
        self.U = np.zeros((self.m, self.M))
        self.D = np.random.rand(self.m, self.M)
        self.V = np.zeros((self.m, self.n))

    def distance(self):
        for j in range(self.m):
            for s in range(self.M):
                self.D[j, s] = np.linalg.norm(self.X[s] - self.V[j]) ** 2

        self.D[self.D < self.epsilon] = self.epsilon

    def membership(self):
        for j in range(self.m):
            for s in range(self.M):
                self.U[j, s] = self.D[j, s] ** (1 / (1 - self.fcm_m)) / np.sum(self.D[:, s] ** (1 / (1 - self.fcm_m)))

    def update_centers(self):
        for j in range(self.m):
            for i in range(self.n):
                self.V[j, i] = np.sum(self.U[j, :] ** self.fcm_m * self.X[:, i]) / np.sum(self.U[j, :] ** self.fcm_m)

    def fit(self):
        self.membership()
        self.update_centers()
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']
        for i in range(self.X.shape[0]):
            for j in range(m):
                if self.U[j, i] == np.max(self.U[:, i]):
                    plt.scatter(self.X[i, 0], self.X[i, 1], c=colors[j])

        for i in range(self.V.shape[0]):
            plt.scatter(self.V[i, 0], self.V[i, 1], c=colors[i], marker='x')
        plt.show()
        for _ in range(self.n_iter):
            self.distance()
            self.membership()

            if np.isnan(self.U).any():
                print("U zawiera wartości nieoznaczone. Przerwanie programu.")
                break

            self.update_centers()

        return self.U, self.V


if __name__ == "__main__":
    spirala = DataSet("spirala.txt", sep="   ")

    sc = StrConv(spirala)
    conv_data = sc.convert_str_to_numbers([0, 1])

    km = KMeans(conv_data, m=4)
    # km.fit()

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']
    X = np.array(conv_data)
    m = 3
    fcm = FuzzyCMeans(m, conv_data)
    U, V = fcm.fit()
    for i in range(X.shape[0]):
        for j in range(m):
            if U[j, i] == np.max(U[:, i]):
                plt.scatter(X[i, 0], X[i, 1], c=colors[j])

    for i in range(V.shape[0]):
        plt.scatter(V[i, 0], V[i, 1], c=colors[i], marker='x')
    plt.show()
