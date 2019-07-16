cmake_minimum_required(VERSION 2.8.12)

if(NOT DEFINED PROJECT_NAME)
  set(NOT_SUBPROJECT ON)
endif()

project(Example)

add_definitions("-std=c++17 -Werror -Wno-error=delete-incomplete")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB_RECURSE EXAMPLE_SOURCES "${CMAKE_CURRENT_LIST_DIR}/example/*.cc")
list(FILTER EXAMPLE_SOURCES EXCLUDE REGEX ".*_test.cc$")
add_library(example STATIC ${EXAMPLE_SOURCES})
target_include_directories(example PUBLIC ${CMAKE_CURRENT_LIST_DIR})

file(GLOB_RECURSE EXAMPLE_TEST_SOURCES "${CMAKE_CURRENT_LIST_DIR}/example/*_test.cc")
add_executable(test ${EXAMPLE_TEST_SOURCES} "${CMAKE_CURRENT_LIST_DIR}/test.cc")
target_link_libraries(test ${CONAN_LIBS} example)

if(NOT_SUBPROJECT)
  install(TARGETS example DESTINATION "${CMAKE_INSTALL_LIBDIR}/example")
  file(GLOB_RECURSE example_headers "${CMAKE_CURRENT_LIST_DIR}/example/*.hpp" "${CMAKE_CURRENT_LIST_DIR}/example/*.ipp" "${CMAKE_CURRENT_LIST_DIR}/example/*.h")
  install(FILES ${example_headers} DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}")
endif(NOT_SUBPROJECT)
