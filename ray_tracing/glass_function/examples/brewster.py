import numpy as np
import matplotlib.pyplot as plt

from pytmm.transferMatrix import *

n = 2
d = 600  # slab thickness, nm
l = 500  # wavelength, nm
ran = np.linspace(0, np.pi/2, 1000)
TE = []
TM = []
for i in ran:
    # TE
    a = TransferMatrix.layer(n, d, l, i, Polarization.s)

    R, T = solvePropagation(a)
    TE.append(np.abs(R**2))

    # TM
    a = TransferMatrix.layer(n, d, l, i, Polarization.p)
    R, T = solvePropagation(a)
    TM.append(np.abs(R**2))


plt.plot(ran, TE)
plt.plot(ran, TM)
plt.xlabel("Angle, rad")
plt.ylabel("Reflectance")
plt.title("Angle dependence of reflectivity")
plt.legend(['TE', 'TM'], loc='best')
plt.show(block=True)