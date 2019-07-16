
cmake_minimum_required(VERSION 3.13)
project(python_example)

SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")

include(${CMAKE_CURRENT_LIST_DIR}/src/example/lib/CMakeLists.txt)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/src/example)

file(GLOB EXAMPLE_PY_SOURCES "src/example/*.cc" "src/example/*.cpp")
find_package(pybind11 REQUIRED)
pybind11_add_module(example_python ${EXAMPLE_PY_SOURCES})
target_link_libraries(example_python PUBLIC example)
