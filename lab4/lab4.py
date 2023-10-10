from SSI.lab3.lab3 import *


class Algorytm11:

    def __init__(self, rozrzut, wsp_przyrostu, iter, zakres_zmiennosci) -> None:
        self.rozrzut = rozrzut
        self.wsp_przyrostu = wsp_przyrostu
        self.iter = iter
        self.zakres_zmiennosci = zakres_zmiennosci

    def f(self, x) -> np.core.numeric:
        return np.sin(x / 10) * np.sin(x / 200)

    def fit(self):
        x = random.uniform(self.zakres_zmiennosci[0], self.zakres_zmiennosci[1])
        y = self.f(x)

        for _ in range(self.iter):
            x_pot = x + random.uniform(-self.rozrzut, self.rozrzut)

            if x_pot > self.zakres_zmiennosci[1]:
                x_pot = self.zakres_zmiennosci[1]
            elif x_pot < self.zakres_zmiennosci[0]:
                x_pot = self.zakres_zmiennosci[0]

            y_pot = self.f(x_pot)

            if y_pot >= y:
                x, y = x_pot, y_pot
                self.rozrzut *= self.wsp_przyrostu
            else:
                self.rozrzut /= self.wsp_przyrostu

            diag = Diagram()
            diag.plot_line_diagram(np.linspace(self.zakres_zmiennosci[0], self.zakres_zmiennosci[1]),
                                   self.f(np.linspace(self.zakres_zmiennosci[0], self.zakres_zmiennosci[1])))
            diag.plot_point_diagram(x, y)
            diag.show_diagram()


if __name__ == "__main__":
    alg = Algorytm11(10, 1.1, 100, [0, 100])
    alg.fit()
