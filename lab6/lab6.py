import numpy as np
import matplotlib.pyplot as plt


def euklides(x0, x1, y0, y1) -> np.core.numeric:
    return np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)


def manhattan(x0, x1, y0, y1):
    return abs(x0 - x1) + abs(y0 - y1)


def miara_niepodobienstwa(ba, bb) -> np.core.numeric:
    miara = 0
    for (pay, pax), el_ba in np.ndenumerate(ba):
        if el_ba == 1:
            odl_min = np.inf
            for (pby, pbx), el_bb in np.ndenumerate(bb):
                if el_bb == 1:
                    odl_akt = euklides(pax, pbx, pay, pby)
                    odl_min = min(odl_min, odl_akt)

            miara += odl_min

    return miara


def miara_podobienstwa_obustronnego(ba, bb) -> np.core.numeric:
    return -(miara_niepodobienstwa(ba, bb) + miara_niepodobienstwa(bb, ba))

def read_data(file_name):
    with open(file_name, "r") as file:
        data = file.read().split("\n\n")

    main_tab = []
    for matrix in data:
        tab = np.array([list(map(int, row.split())) for row in matrix.strip().split('\n')])
        main_tab.append(tab)

    return main_tab

patterns = read_data("patterns.txt")
test = read_data("test.txt")

miary = []
for i in test:
    m = []
    for j in patterns:
        m += [miara_podobienstwa_obustronnego(i, j)]

    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(i, cmap='gray_r')
    ax[0].set_title('Bitmapa testowa')
    ax[1].imshow(patterns[np.argmax(m)], cmap='gray_r')
    ax[1].set_title('Bitmapa wzorcowa')
    plt.show()
