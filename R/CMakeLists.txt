cmake_minimum_required(VERSION 3.13)

include(${CMAKE_CURRENT_LIST_DIR}/src/lib/CMakeLists.txt)
include(${CMAKE_CURRENT_LIST_DIR}/R.CMakeLists.txt)

file(GLOB EXAMPLE_R_SOURCES "src/*.cc" "src/*.cpp")
add_library(dynlib SHARED ${EXAMPLE_SOURCES} ${EXAMPLE_R_SOURCES})
target_link_libraries(dynlib ${CONAN_LIBS})
target_link_options(dynlib PUBLIC ${RLDFLAGS} ${RBLAS} ${RLAPACK} ${RCPPLIBS})
target_include_directories(dynlib PRIVATE ${CMAKE_CURRENT_LIST_DIR}/src ${CMAKE_CURRENT_LIST_DIR}/src/lib)
target_compile_options(dynlib PRIVATE ${RCPPFLAGS} ${RCPPINCL})

install(TARGETS dynlib DESTINATION dynlib)
