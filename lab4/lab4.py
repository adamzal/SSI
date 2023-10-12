from SSI.lab3.lab3 import *


class Algorytm11:

    def __init__(self, rozrzut, wsp_przyrostu, n_iter, zakres_zmiennosci) -> None:
        self.rozrzut = rozrzut
        self.wsp_przyrostu = wsp_przyrostu
        self.n_iter = n_iter
        self.zakres_zmiennosci = zakres_zmiennosci

    @staticmethod
    def f(x) -> np.core.numeric:
        return np.sin(x / 10) * np.sin(x / 200)

    def fit(self):
        x = random.uniform(self.zakres_zmiennosci[0], self.zakres_zmiennosci[1])
        y = self.f(x)

        for _ in range(self.n_iter):
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
                                   self.f(np.linspace(self.zakres_zmiennosci[0], self.zakres_zmiennosci[1])),
                                   "Wykres f(x)")
            diag.plot_point_diagram(x, y, "Ekstremum")
            diag.set_labels("Oś X", "Oś y")
            diag.show_diagram()


class Point:

    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.value = self.f()

    def f(self):
        return np.sin(self.x1 * 0.05) + np.sin(self.x2 * 0.05) + 0.4 * np.sin(self.x1 * 0.15) * np.sin(self.x2 * 0.15)

    def show_point(self):
        print(self.x1, self.x2)


class MuLambda:

    def __init__(self, mu, lambda_, iteracje_liczba, mutacja_poziom, turniej_rozmiar):
        self.mu = mu
        self.lambda_ = lambda_
        self.iteracje_liczba = iteracje_liczba
        self.mutacja_poziom = mutacja_poziom
        self.turniej_rozmiar = turniej_rozmiar
        self.pula_rodzicielska = []

    def inicjuj_pula_rodzicielska(self):
        self.pula_rodzicielska = [Point(np.random.uniform(0, 100), np.random.uniform(0, 100)) for _ in range(self.mu)]

    def mutuj(self, p: Point):
        x1 = p.x1 + np.random.uniform(-self.mutacja_poziom, self.mutacja_poziom)
        x2 = p.x2 + np.random.uniform(-self.mutacja_poziom, self.mutacja_poziom)
        return Point(x1, x2)

    def run(self):
        self.inicjuj_pula_rodzicielska()

        for _ in range(self.iteracje_liczba):
            pula_potomna = []
            for _ in range(self.lambda_):
                oss_turniej = random.sample(self.pula_rodzicielska, self.turniej_rozmiar)
                oss_turniej.sort(key=lambda pt: pt.value, reverse=True)
                pula_potomna.append(self.mutuj(oss_turniej[0]))

            pula_calosc = self.pula_rodzicielska + pula_potomna
            pula_calosc.sort(key=lambda pt: pt.value, reverse=True)

            self.pula_rodzicielska = pula_calosc[:self.mu]

            x1 = np.linspace(0, 100, 100)
            x2 = np.linspace(0, 100, 100)
            X1, X2 = np.meshgrid(x1, x2)

            Z = np.sin(X1 * 0.05) + np.sin(X2 * 0.05) + 0.4 * np.sin(X1 * 0.15) * np.sin(X2 * 0.15)

            plt.figure(figsize=(8, 6))
            contour = plt.contourf(X1, X2, Z, cmap='viridis')
            plt.colorbar(contour, label='Wartość funkcji')

            x1 = []
            x2 = []
            value = []
            for p in self.pula_rodzicielska:
                x1 += [p.x1]
                x2 += [p.x2]
                value += [p.value]

            plt.scatter(x1, x2, marker='s', color='r', s=50, label='rodzice')

            x1 = []
            x2 = []
            value = []
            for p in pula_potomna:
                x1 += [p.x1]
                x2 += [p.x2]
                value += [p.value]

            plt.scatter(x1, x2, marker='x', color='b', s=50, label='potomkowie')

            plt.legend()
            plt.xlabel('x1')
            plt.ylabel('x2')
            plt.title(f'Rzut funkcji na płaszczyznę. Najlepszy wynik {self.pula_rodzicielska[0].value} '
                      f'dla \n x1={self.pula_rodzicielska[0].x1} x2={self.pula_rodzicielska[0].x2}')
            plt.show()

        return self.pula_rodzicielska[0]


if __name__ == "__main__":
    alg = Algorytm11(10, 1.1, 100, [0, 100])
    # alg.fit()

    alg2 = MuLambda(mu=8, lambda_=15, turniej_rozmiar=4, mutacja_poziom=10, iteracje_liczba=20)
    # alg2.run()
