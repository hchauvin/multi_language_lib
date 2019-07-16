#! /usr/bin/env python3

import os
import re
import sys
import sysconfig
import platform
import subprocess
import shutil

from distutils.version import LooseVersion
from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from setuptools.command.test import test as TestCommand
from shutil import copyfile, copymode


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError(
                "CMake must be installed to build the following extensions: " +
                ", ".join(e.name for e in self.extensions))

        if platform.system() == "Windows":
            cmake_version = LooseVersion(re.search(r'version\s*([\d.]+)',
                                         out.decode()).group(1))
            if cmake_version < '3.1.0':
                raise RuntimeError("CMake >= 3.1.0 is required on Windows")

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(
            os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
                      '-DPYTHON_EXECUTABLE=' + sys.executable,
                      '-G', 'Unix Makefiles']

        cfg = 'Debug' if self.debug else 'Release'
        build_args = ['--config', cfg]

        if platform.system() == "Windows":
            cmake_args += ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(
                cfg.upper(),
                extdir)]
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
            build_args += ['--', '/m']
        else:
            cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
            build_args += ['--', '-j2']

        env = os.environ.copy()
        env['CXXFLAGS'] = '{} -DVERSION_INFO=\\"{}\\"'.format(
            env.get('CXXFLAGS', ''),
            self.distribution.get_version())
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(['conan', 'install', os.path.join(ext.sourcedir, 'src/example/lib'), '--build=outdated'], cwd=self.build_temp)
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, env=env, cwd=self.build_temp)
        subprocess.check_call(['cmake', '--build', '.', '--target', 'example'] + build_args, cwd=self.build_temp)
        for file_name in os.listdir(os.path.join(self.build_temp, 'lib')):
            full_file_name = os.path.join(self.build_temp, 'lib', file_name)
            if os.path.isfile(full_file_name):
                if os.path.isfile(os.path.join(extdir, file_name)):
                    os.unlink(os.path.join(extdir, file_name))
                shutil.copy(full_file_name, os.path.join(extdir, file_name))
        print()  # Add an empty line for cleaner output

setup(
    name='example',
    version='0.1.0',
    author='Hadrien Chauvin',
    author_email='hadrien@chauvin.io',
    description='Example package',
    long_description='',
    packages=find_packages('src'),
    package_dir={'':'src'},
    ext_modules=[CMakeExtension('example/example')],
    cmdclass=dict(build_ext=CMakeBuild),
    test_suite='tests',
    zip_safe=False,
    install_requires=['pybind11==2.3.0'],
)
