cmake_minimum_required(VERSION 3.15)
project(imnodes LANGUAGES CXX)

include(GNUInstallDirs)

# Find ImGui (Conan will provide this via CMakeDeps)
find_package(imgui REQUIRED)

# Define the imnodes library
add_library(imnodes imnodes.cpp)

# Add macro needed for operator overloading (globally for this target)
target_compile_definitions(imnodes PRIVATE IMGUI_DEFINE_MATH_OPERATORS)

# Include the current source dir for the headers
target_include_directories(imnodes PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
    $<INSTALL_INTERFACE:include>
)

# Link to imgui
target_link_libraries(imnodes PUBLIC imgui::imgui)

# Export target
install(TARGETS imnodes EXPORT imnodesTargets)

# Export config for find_package(imnodes)
install(EXPORT imnodesTargets
    FILE imnodesTargets.cmake
    NAMESPACE imnodes::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/imnodes
)

# Install headers
install(FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/imnodes.h
    ${CMAKE_CURRENT_SOURCE_DIR}/imnodes_internal.h
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
