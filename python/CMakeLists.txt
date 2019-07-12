
cmake_minimum_required(VERSION 3.13)
project(python_example)

include(${CMAKE_CURRENT_LIST_DIR}/src/example/lib/CMakeLists.txt)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY /Users/hadrienchauvin/code/multi_language_lib/python/src/example)

file(GLOB EXAMPLE_PY_SOURCES "src/example/*.cc" "src/example/*.cpp")
find_package(pybind11 REQUIRED)
pybind11_add_module(example ${EXAMPLE_SOURCES} ${EXAMPLE_PY_SOURCES})
target_include_directories(example PRIVATE ${CMAKE_CURRENT_LIST_DIR}/src/example ${CMAKE_CURRENT_LIST_DIR}/src/example/lib ${PYTHON_INCLUDE_DIRS})
