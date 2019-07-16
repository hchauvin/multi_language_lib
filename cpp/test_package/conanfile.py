from conans import ConanFile, CMake
import os


class ExampleTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "example/0.1.0@hchauvin/test"
    generators = "cmake"

    def build(self):
        self.cmake = CMake(self)
        self.cmake.configure()
        self.cmake.build()

    def test(self):
        self.cmake.build(target="main")
        self.run(os.path.join(".", "bin", "main"))
