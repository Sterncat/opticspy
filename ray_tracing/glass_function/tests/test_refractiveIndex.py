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


from unittest import TestCase

from pytmm.refractiveIndex import *


class TestRefractiveIndex(TestCase):
    def test_defaultInit(self):
        database = RefractiveIndex()
        assert os.path.exists(database.referencePath)
        assert os.path.exists(os.path.join(database.referencePath, os.path.normpath("library.yml")))
        assert os.path.isfile(os.path.join(database.referencePath, os.path.normpath("library.yml")))

    def test_getMaterialFilename(self):
        database = RefractiveIndex()
        for sh in database.catalog:
            for b in sh['content']:
                if 'DIVIDER' not in b:
                    for p in b['content']:
                        if 'DIVIDER' not in p:
                            mat = database.getMaterialFilename(sh['SHELF'], b['BOOK'], p['PAGE'])
                            assert os.path.exists(os.path.normpath(mat))
                            assert os.path.isfile(os.path.normpath(mat))

    def test_getMaterial(self):
        database = RefractiveIndex()
        for sh in database.catalog:
            for b in sh['content']:
                if 'DIVIDER' not in b:
                    for p in b['content']:
                        if 'DIVIDER' not in p:
                            try:
                                matfile = database.getMaterialFilename(sh['SHELF'], b['BOOK'], p['PAGE'])
                                mat = database.getMaterial(sh['SHELF'], b['BOOK'], p['PAGE'])
                            except Exception as err:
                                print(matfile)
                                print(err)
                                raise err
