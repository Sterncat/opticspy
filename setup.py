#!/usr/bin/env python

from distutils.command import build_ext
from distutils.command.build import build
from distutils.command.install_data import install_data
from distutils.core import setup
import numpy
from os.path import join, split
import sys, platform, os

from distutils.command.install_headers import install_headers
from distutils.util import get_platform


class opticspy_install_data(install_data):
    def run(self):
        # Call parent
        #self.run_command('install_headers')
        install_data.run(self)
        # Execute commands


def distutils_dir_name(dname):
    """Returns the name of a distutils build directory"""
    f = "{dirname}.{platform}-{version[0]}.{version[1]}"
    return f.format(dirname=dname,
                    platform=get_platform(),
                    version=sys.version_info)


class opticspy_install_headers(install_headers):

    def initialize_options(self):
        pass
        #self.install_dir
        #self.force = 0
        #self.outfiles = []

    def run(self):
        # Call parent
        #print "distribution.headers = ", self.distribution.headers
        install_headers.run(self)
        # Execute commands

class my_build_ext(build_ext.build_ext):
    pass

# Subclass the build command to ensure that build_ext produces
class my_build(build):
    def run(self):
        self.run_command('build_ext')
        build.run(self)



semifem_dist = setup(name = "opticspy",
      version = "0.1",
      description = "Python optics module ",
      author = "Xing Fan",
      author_email = "marvin.fanxing@gmail.com",
      url = "https://github.com/Sterncat/opticspy",
      packages = ["opticspy",
                  "opticspy.lens","opticspy.mplot3d",
                  "opticspy.ray_tracing",
                  ],
      package_dir={},
      package_data={},
      headers=[],
                     
      data_files=[],
      #scripts = scripts,

      include_dirs=[],

      ext_modules = [],

     cmdclass = {"build": my_build, "build_ext": my_build_ext,
                 "install_data": opticspy_install_data,
                 "install_headers": opticspy_install_headers,
                 },

)