import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg


class Sterownik:

    def __init__(self, pojazd):
        self.x_min = -100
        self.x_max = 100
        self.x_zasieg = 200
        self.y_min = -100
        self.y_max = 0
        self.y_zasieg = 100
        self.rampa_lewy_x = -30
        self.rampa_prawy_x = 30
        self.rampa_dol_y = -10
        self.rampa_gora_y = 0
        self.rampa_kat_docelowy_min = -20
        self.rampa_kat_docelowy_max = 20
        self.obrot_min = -20
        self.obrot_max = 20
        self.ruch_skok = 5.0
        self.error_length = 3
        self.pojazd = pojazd
        self.x = []
        self.y = []

    def rysuj_plansze(self):
        fig, ax = plt.subplots()
        ax.plot([self.rampa_lewy_x, self.rampa_lewy_x, self.rampa_prawy_x, self.rampa_prawy_x],
                [self.rampa_gora_y, self.rampa_dol_y, self.rampa_dol_y, self.rampa_gora_y])
        imagebox = OffsetImage(self.pojazd.obraz, zoom=0.2)
        ab = AnnotationBbox(imagebox, (self.pojazd.x, self.pojazd.y), frameon=False)
        ax.add_artist(ab)
        ax.set_xlim(self.x_min, self.x_max)
        ax.set_ylim(self.y_min, self.y_max)
        ax.plot(self.x, self.y)
        plt.show()

    @staticmethod
    def euklides_norm(x0, x1, y0, y1) -> np.core.numeric:
        return np.sqrt((float(x0) - float(x1)) ** 2 + (float(y0) - float(y1)) ** 2)

    def zwroc_odpowiedz(self):
        x, y, kat = self.pojazd.x, self.pojazd.y, self.pojazd.kat

        x_docelowe = (self.rampa_lewy_x + self.rampa_prawy_x) / 2
        y_docelowe = (self.rampa_gora_y + self.rampa_dol_y) / 2

        kat_do_celu = math.degrees(math.atan((x_docelowe - x) / (y_docelowe - y)))

        if kat_do_celu < kat and (kat - kat_do_celu) >= self.obrot_max:
            return self.obrot_min
        elif kat_do_celu > kat and (kat_do_celu - kat) >= self.obrot_max:
            return self.obrot_max
        elif kat_do_celu < kat and self.obrot_min < (kat - kat_do_celu) < self.obrot_max:
            return - (kat - kat_do_celu)
        elif kat_do_celu > kat and self.obrot_min < (kat_do_celu - kat) < self.obrot_max:
            return kat_do_celu - kat

        return 0

    def run(self):
        x, y = self.pojazd.x, self.pojazd.y
        x_docelowe = (self.rampa_lewy_x + self.rampa_prawy_x) / 2
        y_docelowe = (self.rampa_gora_y + self.rampa_dol_y) / 2
        while not ((self.rampa_lewy_x + self.error_length <= x <= self.rampa_prawy_x - self.error_length)
                   and (self.rampa_dol_y + self.error_length <= y <= self.rampa_gora_y - self.error_length)):
            x, y, kat = self.pojazd.x, self.pojazd.y, self.pojazd.kat
            obrot = self.zwroc_odpowiedz()
            self.pojazd.kat += obrot
            self.x.append(x)
            self.y.append(y)

            if self.euklides_norm(x_docelowe, x, y_docelowe, y) >= self.ruch_skok:
                if kat <= 90:
                    self.pojazd.x += math.cos(math.radians(90-kat)) * self.ruch_skok
                    self.pojazd.y += math.sin(math.radians(90-kat)) * self.ruch_skok
                elif 90 < kat <= 180:
                    self.pojazd.x += math.cos(math.radians(kat - 90)) * self.ruch_skok
                    self.pojazd.y += math.sin(math.radians(kat - 90)) * self.ruch_skok
            else:
                if kat <= 90:
                    self.pojazd.x += math.cos(
                        math.radians(90-kat)) * self.euklides_norm(x_docelowe, x, y_docelowe, y)
                    self.pojazd.y += math.sin(
                        math.radians(90-kat)) * self.euklides_norm(x_docelowe, x, y_docelowe, y)
                elif 90 < kat <= 180:
                    self.pojazd.x += math.cos(
                        math.radians(kat - 90)) * self.euklides_norm(x_docelowe, x, y_docelowe, y)
                    self.pojazd.y += math.sin(
                        math.radians(kat - 90)) * self.euklides_norm(x_docelowe, x, y_docelowe, y)


class PojazdPolozenie:

    def __init__(self, x, y, kat):
        self.x = x
        self.y = y
        self.kat = kat
        self.obraz = mpimg.imread('samochod.png')


pojazd = PojazdPolozenie(70, -100, 30)
S = Sterownik(pojazd)

S.run()
S.rysuj_plansze()
