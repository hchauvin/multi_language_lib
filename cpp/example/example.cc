/*
 * Copyright (c) Hadrien Chauvin
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#include <boost/algorithm/string.hpp>

#include "example/example.hpp"

namespace example {

std::vector<std::string> split(std::string s) {
  std::vector<std::string> ans();
  boost::split(ans, s, boost::is_any_of("\t "));
}

} // example
