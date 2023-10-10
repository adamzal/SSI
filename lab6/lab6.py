import numpy as np

z_w_1 = np.array([
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
])

z_w_2 = np.array([
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
])

z_w_3 = np.array([
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 0]
])

z_t_1 = np.array([
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
])

z_t_2 = np.array([
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1]
])

z_t_3 = np.array([
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1]
])


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


print(miara_niepodobienstwa(z_t_2, z_w_1))
print(miara_niepodobienstwa(z_w_1, z_t_2))
print(miara_podobienstwa_obustronnego(z_w_1, z_t_2))

template_bitmaps = [z_w_1, z_w_2, z_w_3]
test_bitmaps = [z_t_1, z_t_2, z_t_3]

miary = []
for i in test_bitmaps:
    m = []
    for j in template_bitmaps:
        m += [miara_podobienstwa_obustronnego(i, j)]

    print(f"Bitmapa testowa \n {i} \n jest najbardziej podobna "
          f"do bitmapy wzorcowej \n {template_bitmaps[np.argmax(m)]} \n")
