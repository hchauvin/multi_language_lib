/*
 * Copyright (c) Hadrien Chauvin
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "example/example.hpp"

namespace py = pybind11;

PYBIND11_MODULE(example, m) {
  m.def("split", example::split);
}
