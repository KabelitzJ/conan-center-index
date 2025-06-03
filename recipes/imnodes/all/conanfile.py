from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import get, copy, replace_in_file
from conan.tools.scm import Version
import os

class ImnodesConan(ConanFile):
    name = "imnodes"
    version = "0.5.0-docking"
    license = "MIT"
    url = "https://github.com/Nelarius/imnodes"
    description = "Immediate Mode Graph Node Editor for Dear ImGui"
    topics = ("imgui", "node-editor", "gui")

    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "CMakeLists.txt", "imnodes.cpp", "imnodes.h", "imnodes_internal.h"  # local dev
    package_type = "library"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
         "fPIC": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
    }

    def layout(self):
        cmake_layout(self)

    def export_sources(self):
        copy(self, "CMakeLists.txt", self.recipe_folder, self.export_sources_folder)

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def requirements(self):
        if Version(self.version) == "0.5.0-docking":
            self.requires("imgui/1.91.5-docking", transitive_headers=True)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["imnodes"]
