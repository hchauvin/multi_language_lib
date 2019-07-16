cmake_minimum_required(VERSION 2.8.12)
project(Example)

add_definitions("-std=c++17 -Werror -Wno-error=delete-incomplete")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB_RECURSE EXAMPLE_SOURCES "${CMAKE_CURRENT_LIST_DIR}/example/*.cc")
list(FILTER EXAMPLE_SOURCES EXCLUDE REGEX ".*_test.cc$")
add_library(example STATIC ${EXAMPLE_SOURCES})

install(TARGETS example DESTINATION lib)
list(GLOB_RECURSE example_headers "${CMAKE_CURRENT_LIST_DIR}/example/*.hpp" "${CMAKE_CURRENT_LIST_DIR}/example/*.ipp" "${CMAKE_CURRENT_LIST_DIR}/example/*.h")
install(FILES ${example_headers} DESTINATION include)

file(GLOB_RECURSE EXAMPLE_TEST_SOURCES "${CMAKE_CURRENT_LIST_DIR}/example/*_test.cc")
add_executable(test ${EXAMPLE_TEST_SOURCES} "${CMAKE_CURRENT_LIST_DIR}/test.cc")
target_link_libraries(test ${CONAN_LIBS} example)
target_include_directories(test PUBLIC ${CMAKE_CURRENT_LIST_DIR})
