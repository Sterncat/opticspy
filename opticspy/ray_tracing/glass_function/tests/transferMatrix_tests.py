#    This file is part of PyTMM.
#
#    PyTMM is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PyTMM is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
#
#   Copyright 2014-2015 Pavel Dmitriev <pavel.a.dmitriev@gmail.com>

import matplotlib.pyplot as plt

from pytmm.transferMatrix import *
from refractiveIndex import *

catalog = RefractiveIndex()
si = catalog.getMaterial('main', 'Si', 'Aspnes')

r, t = [], []
r1, t1 = [], []
r2, t2 = [], []
r3, t3 = [], []


# single layer
wavelengths = numpy.linspace(100, 900, num=2000)
for i in wavelengths:
    a = TransferMatrix.layer(1.46, 2000, i)
    b = TransferMatrix.layer(1.46 - 0.001j, 2000, i)
    c = TransferMatrix.layer(1.46 - 0.01j, 2000, i)
    d = TransferMatrix.layer(1.46 - 0.1j, 2000, i)

    R = solvePropagation(a)[0]
    r.append(numpy.abs(R) ** 2)
    R = solvePropagation(b)[0]
    r1.append(numpy.abs(R) ** 2)
    R = solvePropagation(c)[0]
    r2.append(numpy.abs(R) ** 2)
    R = solvePropagation(d)[0]
    r3.append(numpy.abs(R) ** 2)

    # res2 = solvePropagation(e)
    # b = findReciprocalTransferMatrix(res1[1], res1[0])

    # c = findGeneralizedTransferMatrix(res1[1], res1[0], res2[1], res2[0],
    #                                   bottomMat2=TransferMatrix.layer(1.46-1j*47, 1000, i))

    # res3 = solvePropagation(c)

    # R = numpy.abs(res3[1]-res1[1])

plt.plot(wavelengths, r)
plt.plot(wavelengths, r1)
plt.plot(wavelengths, r2)
plt.plot(wavelengths, r3)
plt.legend(['1.46', '1.46-0.001j', '1.46-0.01j', '1.46-0.1j'])
plt.show()
