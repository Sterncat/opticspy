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


import numpy
import enum

class Polarization(enum.Enum):
    s = 0
    p = 1

class TransferMatrix:
    """
        Dielectric layer TMM

        How the functions eat structure matricies:

        | T |   |        | |        | |     |   | 1 |
        |   | = | Bottom | | Matrix | | Top | = |   |
        | 0 |   |        | |        | |     |   | R |

    """

    @staticmethod
    def structure(*args):
        """
        args - separate structure matricies
        Left to Right = Bottom to Top
        :param args:
        """
        mat = numpy.identity(2, dtype=numpy.complex128)
        for m in args:
            mat = numpy.dot(m.matrix, mat)
        return TransferMatrix(mat)

    @staticmethod
    def layer(n, d, wavelength, theta=0, pol=Polarization.s):
        """
        Creates a Air-DielectricLayer-Air Transfer Matrix
        :param n:
        :param d:
        :param wavelength:
        """
        bottomBoundary = TransferMatrix.boundingLayer(1, n, theta, pol)
        topBoundary = TransferMatrix.boundingLayer(n, 1, theta, pol)
        propagation = TransferMatrix.propagationLayer(n, d, wavelength, theta, pol)

        return TransferMatrix.structure(bottomBoundary,
                                        propagation,
                                        topBoundary)

    @staticmethod
    def boundingLayer(n1, n2, theta=0, pol=Polarization.s):
        """
        Creates a DielectricLayer-DielectricLayer Boundary Transfer Matrix
        :param n1:
        :param n2:
        """
        # if numpy.abs((n1/n2)*numpy.sin(theta)) >= 1.0:
        #     theta2 = numpy.pi/2 * numpy.sign(numpy.sin(theta))
        # else:
        theta2 = numpy.arcsin((n1/n2)*numpy.sin(theta), dtype=numpy.complex128)

        # TE
        if pol is Polarization.s:
            _n1 = n1*numpy.cos(theta)
            _n2 = n2*numpy.cos(theta2)
            a21 = 1

        # TM
        elif pol is Polarization.p:
            _n1 = n1/numpy.cos(theta)
            _n2 = n2/numpy.cos(theta2)
            a21 = numpy.cos(theta2)/numpy.cos(theta)


        boundary = 1/(2 * a21 * _n2) *numpy.array([[(_n1 + _n2), (_n2 - _n1)],
                                    [(_n2 - _n1), (_n1 + _n2)]], dtype=numpy.complex128)
        return TransferMatrix(boundary)

    @staticmethod
    def propagationLayer(n, d, wavelength, theta=0, pol=Polarization.s):
        """
        Creates a Propagation Transfer Matrix, width d, refractive index n
        :param n:
        :param d:
        :param wavelength:
        """
        theta2 = numpy.arcsin((1/n)*numpy.sin(theta), dtype=numpy.complex128)

        propagation = numpy.array([[numpy.exp((-1j * n * d * 2 * numpy.pi / wavelength) * numpy.cos(theta2)), 0],
                                   [0, numpy.exp((1j * n * d * 2 * numpy.pi / wavelength) * numpy.cos(theta2))]],
                                  dtype=numpy.complex128)
        return TransferMatrix(propagation)

    def __init__(self, matrix):
        self.matrix = matrix

    def invert(self):
        """
        Inverts matrix

        """
        self.matrix = numpy.linalg.inv(self.matrix)

    def appendLeft(self, matrix):
        """

        :param matrix:
        """
        self.matrix = numpy.dot(matrix.matrix, self.matrix)

    def appendRight(self, matrix):
        """

        :param matrix:
        """
        self.matrix = numpy.dot(self.matrix, matrix.matrix)


def solvePropagation(transferMatrix, incidentField=1.0):
    """Calculate reflectance and transmittance
    :param transferMatrix:
    :param incidentField:
    """
    # res[1] = transmittance, res[0] = reflectance
    lhs = numpy.array([[transferMatrix.matrix[0, 1], -1],
                       [transferMatrix.matrix[1, 1], 0]])
    rhs = numpy.array([-transferMatrix.matrix[0, 0], -transferMatrix.matrix[1, 0]])
    rhs = numpy.multiply(rhs, incidentField)
    res = numpy.linalg.solve(lhs, rhs)
    reflectance = res[0]
    transmittance = res[1]
    return reflectance, transmittance


def findReciprocalTransferMatrix(transmittance, reflectance, bottomMat=TransferMatrix(numpy.identity(2)),
                                 topMat=TransferMatrix(numpy.identity(2))):  # , incidentField=1.0
    """

    :param transmittance:
    :param reflectance:
    :param bottomMat:
    :param topMat:
    :return:
    """
    assert transmittance != 0

    matrix = numpy.array([[1 / numpy.conj(transmittance), reflectance / transmittance],
                          [numpy.conj(reflectance / transmittance), 1 / transmittance]])
    matrix = numpy.dot(numpy.linalg.inv(bottomMat.matrix), matrix)
    matrix = numpy.dot(matrix, numpy.linalg.inv(topMat.matrix))
    return TransferMatrix(matrix)


def findReciprocalTransferMatrixLegacy(transmittance, reflectance, bottomMat=TransferMatrix(numpy.identity(2)),
                                       topMat=TransferMatrix(numpy.identity(2))):  # , incidentField=1.0
    """

    :param transmittance:
    :param reflectance:
    :param bottomMat:
    :param topMat:
    :return:
    """
    a = numpy.identity(2)
    b = numpy.array([[numpy.real(reflectance), numpy.imag(reflectance)],
                     [numpy.imag(reflectance), -numpy.real(reflectance)]])
    lhs = numpy.vstack((numpy.hstack((a, b)), numpy.hstack((b, a))))
    rhs = numpy.array([numpy.real(transmittance), numpy.imag(transmittance), 0, 0])
    res = numpy.linalg.solve(lhs, rhs)
    matrix = numpy.array([[res[0] + 1j * res[1], res[2] - 1j * res[3]],
                          [res[2] + 1j * res[3], res[0] - 1j * res[1]]])

    matrix = numpy.dot(numpy.linalg.inv(bottomMat.matrix), matrix)
    matrix = numpy.dot(matrix, numpy.linalg.inv(topMat.matrix))
    return TransferMatrix(matrix)


def findGeneralizedTransferMatrix(transmitance1, reflectance1, transmitance2, reflectance2,
                                  bottomMat1=TransferMatrix(numpy.identity(2)),
                                  topMat1=TransferMatrix(numpy.identity(2)),
                                  bottomMat2=TransferMatrix(numpy.identity(2)),
                                  topMat2=TransferMatrix(numpy.identity(2))):
    """

    :param transmitance1:
    :param reflectance1:
    :param transmitance2:
    :param reflectance2:
    :param bottomMat1:
    :param topMat1:
    :param bottomMat2:
    :param topMat2:
    :return:
    """
    a12 = numpy.dot(numpy.linalg.inv(bottomMat1.matrix), numpy.array([[transmitance1], [0]]))
    a34 = numpy.dot(numpy.linalg.inv(bottomMat2.matrix), numpy.array([[transmitance2], [0]]))

    b12 = numpy.dot(topMat1.matrix, numpy.array([[1], [reflectance1]]))
    b34 = numpy.dot(topMat2.matrix, numpy.array([[1], [reflectance2]]))

    rhs = numpy.array([a12[0, 0], a34[0, 0], a12[1, 0], a34[1, 0]])

    bmat = numpy.array([[b12[0, 0], b12[1, 0]],
                        [b34[0, 0], b34[1, 0]]])

    lhs = numpy.vstack((numpy.hstack((bmat, numpy.zeros((2, 2)))),
                        numpy.hstack((numpy.zeros((2, 2)), bmat))))
    res = numpy.linalg.solve(lhs, rhs)

    mat = numpy.array([[res[0], res[2]],
                       [res[1], res[3]]])
    return TransferMatrix(mat)
