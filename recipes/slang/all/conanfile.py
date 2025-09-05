from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout, CMakeDeps, CMakeToolchain
from conan.tools.scm import Git
from conan.tools.files import chdir, copy, collect_libs
import os


class SlangConan(ConanFile):
    name = "slang"
    version = "0.9"   # or use "master" if you prefer latest
    license = "MIT"
    url = "https://github.com/MikePopoloski/slang"
    description = "C++20-based SystemVerilog compiler and toolchain"
    topics = ("systemverilog", "compiler", "hdl", "verilog")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
    }
    default_options = {
        "shared": False,
    }

    def layout(self):
        cmake_layout(self)

    def source(self):
        git = Git(self)
        if not os.path.exists("slang"):
            git.clone(url=self.url, target="slang")
        with chdir(self, "slang"):
            git.checkout("v9.0")  # or "v0.9" etc.

    def requirements(self):
        self.requires("mimalloc/2.1.9")
        self.requires("fmt/11.2.0", transitive_headers=True, transitive_libs=True)

    def generate(self):
        deps = CMakeDeps(self)
        toolchain = CMakeToolchain(self)

        deps.generate()
        toolchain.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure(
            build_script_folder="slang", 
            variables={
                "SLANG_INCLUDE_INSTALL": "ON"
            }
        )
        cmake.build()

    def package(self):
        copy(self, "LICENSE.txt", src="slang", dst=os.path.join(self.package_folder, "licenses"))
        cmake = CMake(self)
        cmake.install()


    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
