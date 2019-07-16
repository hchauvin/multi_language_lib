import os
from conans import ConanFile, CMake


class ExampleConan(ConanFile):
    name = "example"
    version = "0.1.0"
    url = "https://github.com/hchauvin/multi_language_lib"
    author = "hchauvin"
    license = "MIT"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake", "VSCodeProperties"
    exports = "*"
    description = "Example lib"
    requires = (
        "vscodepropertiesgen/0.1@mkovalchik/stable",
        "boost/1.67.0@conan/stable",  # Cannot use 1.68.0 because of wrong linking order
        "catch2/2.4.2@bincrafters/stable",
        "pybind11/2.3.0@conan/stable",
    )

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include")
        self.copy("*.ipp", dst="include")
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.dylib", dst="bin", src="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
