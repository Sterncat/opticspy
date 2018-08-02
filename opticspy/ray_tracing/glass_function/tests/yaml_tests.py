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

from pytmm.refractiveIndex import *

# catalog = RefractiveIndex("../RefractiveIndex")
catalog = RefractiveIndex()
mat = catalog.getMaterial('other', 'pmma_resists', 'Microchem495')
print(mat.getRefractiveIndex(500))
# f = open('Hass.yml')
# a = yaml.safe_load(f)
# f.close()
# print(a)

# print(mat.getExtincionCoefficient(500))


#
# Iterate the shit out of the catalog
#
i = 0
for sh in catalog.catalog:
    for b in sh['content']:
        if 'DIVIDER' not in b:
            for p in b['content']:
                if 'DIVIDER' not in p:
                    try:
                        mat = catalog.getMaterial(sh['SHELF'], b['BOOK'], p['PAGE'])
                        a = mat.getRefractiveIndex(
                            (mat.refractiveIndex.rangeMin + mat.refractiveIndex.rangeMax) * 1000.0 / 2)
                        # b = mat.getExtinctionCoefficient((mat.extinctionCoefficient.rangeMin
                        #       + mat.extinctionCoefficient.rangeMax)*1000.0/2)
                    except FormulaNotImplemented:
                        pass
                    except NoExtinctionCoefficient:
                        pass
                    except (Exception, NotImplementedError) as inst:
                        print("caught exception in {}".format(p['path']))
                        print(inst)
                        i += 1
                        pass

print('Caught {} exceptions while parsing catalog'.format(i))
