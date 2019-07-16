cmake_minimum_required(VERSION 2.8.12)
project(ExampleTest)

add_definitions("-std=c++17 -Werror -Wno-error=delete-incomplete")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(main main.cc)
target_link_libraries(main ${CONAN_LIBS} example)
