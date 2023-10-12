import numpy as np


class FireflyaAlgorithm:

    def __init__(self, N, beta0, gamma0, mu0, xmin, xmax, iteracje_liczba):
        self.N = N
        self.n = 2
        self.beta0 = beta0
        self.gamma0 = gamma0
        self.mu0 = mu0
        self.xmin = xmin
        self.xmax = xmax
        self.iteracje_liczba = iteracje_liczba
        self.gamma = gamma0 / (xmax - xmin)
        self.mu = mu0 * (xmax - xmin)
        self.X = np.random.uniform(xmin, xmax, (N, self.n))
        self.F = np.array([self.f(x[0], x[1]) for x in self.X])
        self.best_point = self.X[np.argmax(self.F)]
        self.best_value = np.max(self.F)

    @staticmethod
    def f(x1, x2):
        return np.sin(x1 * 0.05) + np.sin(x2 * 0.05) + 0.4 * np.sin(x1 * 0.15) * np.sin(x2 * 0.15)

    @staticmethod
    def euklides_norm(x1, x2):
        return np.sqrt((x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2)

    def run(self):
        for _ in range(self.iteracje_liczba):
            for a in range(self.N):
                for b in range(self.N):
                    if self.F[b] > self.F[a]:
                        r = self.euklides_norm(self.X[a], self.X[b])
                        beta = self.beta0 * np.exp(-self.gamma * r ** 2)
                        self.X[a] += beta * (self.X[b] - self.X[a])
                self.X[a] += np.random.uniform(-self.mu, self.mu, self.n)
                self.F[a] = self.f(self.X[a][0], self.X[a][1])
                if self.F[a] > self.best_value:
                    self.best_point = self.X[a]
                    self.best_value = self.F[a]

        return self.best_point, self.best_value


if __name__ == "__main__":
    fa = FireflyaAlgorithm(4, .3, .1, .05, 0, 100, 30)
    best_point, best_value = fa.run()

    print(f'Najlepszy punkt: x1 = {best_point[0]}, x2 = {best_point[1]}')
    print(f'Najlepsza wartość funkcji: {best_value}')
