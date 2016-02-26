import numpy as np
import matplotlib.pyplot as plt

from pytmm.transferMatrix import *

n1 = 1.5
n2 = np.sqrt(n1)
d = 700 / (n2 * 4)     # quarter-wavelength coating

ran = range(200, 1600, 1)
refl0 = []
refl = []
for i in ran:
    # substrate layer (considered infinite, so only bounding layer needed)
    a = TransferMatrix.boundingLayer(1, n1)

    R, T = solvePropagation(a)
    refl0.append(np.abs(R**2))

    # antireflective layer layer "left" of substrate
    b = TransferMatrix.layer(n2, d, i)
    a.appendRight(b)

    R, T = solvePropagation(a)
    refl.append(np.abs(R**2))


plt.plot(ran, refl0)
plt.plot(ran, refl)
plt.xlabel("Wavelength, nm")
plt.ylabel("Reflectance")
plt.title("Reflectance of ideal single-layer antireflective coating")
plt.legend(['Substrate', 'Coated substrate'], loc='best')
plt.show(block=True)