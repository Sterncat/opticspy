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

function refractiveIndex = getRefractiveIndex(catalog, section, book, page, wavelength)
    %Usage getRefractiveIndex('path-to-refractive-index-database', 'main', 'SiO2', 'Malitson', 750s)
    refractiveIndex = python('refractiveIndex.py', catalog, section, book, page, num2str(wavelength));
end