from conans import ConanFile, CMake
import os


class ExampleTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "example/0.1.0@hchauvin/test"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.cmake.build(target="test")
        self.run(os.path.join(".", "bin", "main"))
